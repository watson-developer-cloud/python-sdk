"""
This example code implements a command line runnable script that can be used to run learning-to-rank experiments
 using the /rank API methods available as part of the Retrieve and Rank service.  See usage details by running
 python rank_with_evaluation_v1.py --help
"""
import argparse
import csv
import json
import logging
import math
import sys
import tempfile
from collections import defaultdict
from time import sleep

from watson_developer_cloud import RetrieveAndRankV1, WatsonException

BLUEMIX_CONNECTION = None
_MAX_RUNTIME_ATTEMPTS = 1
_QID_COL_INDEX = 0
_LABEL_COL_INDEX = -1
_ANS_ID_COL_INDEX = 0
_TOP_K_FOR_METRICS = 5


def train_ranker(train_file, is_enabled_make_space=False):
    """
    Method submits POST request to create a new ranker using the input training file. Then polls the service
        waiting for training to complete. Raises exception if ranker training fails.

    :param file train_file: filepath to the training file in csv format (qid,feature1,feature2...,label)
    :param bool is_enabled_make_space: boolean which decides if pre-existing rankers can be deleted to make space
        space for a new ranker.
    :return: ranker id that can be used to access to the ranker in bluemix
    :rtype: str
    """
    LOGGER.info("Submitting request to create a new ranker trained with file %s" % train_file)

    try:
        response = BLUEMIX_CONNECTION.create_ranker(training_data=train_file, name='RANKER-EXPERIMENT')
        LOGGER.info("Training request submitted successfully for ranker id:<<%s>>" % response['ranker_id'])
        if LOGGER.isEnabledFor(logging.DEBUG):
            print(json.dumps(response, indent=2))
        return response['ranker_id']

    except WatsonException as ex:
        LOGGER.error("Training failed with response: %s" % ex.message)

        # Check if quota is full & make space if deletion is enabled
        if "This user or service instance has the maximum number of rankers" in ex.message:
            if is_enabled_make_space:
                LOGGER.warn("Quota is full. Deleting all previous rankers to make space.")
                _delete_existing_rankers()
                train_file.seek(0)  # rewind the file handler so that we can make another request
                return train_ranker(train_file, False)
            else:
                LOGGER.error("Quota is full. Use the '-r' parameter to make space by deleting all previous rankers.")
                raise ex
        else:
            raise ex


def _delete_existing_rankers():
    """
    Helper method deletes pre-existing rankers under this bluemix url for this user. Expects at least one pre-existing
    ranker to be found.
    """
    previously_created_rankers = BLUEMIX_CONNECTION.list_rankers()['rankers']

    LOGGER.debug("Found %d previously created rankers" % len(previously_created_rankers))
    for ranker in previously_created_rankers:
        response = BLUEMIX_CONNECTION.delete_ranker(ranker['ranker_id'])
        if LOGGER.isEnabledFor(logging.DEBUG):
            print(json.dumps(response, indent=2))

    LOGGER.info("Deleted %d rankers successfully" % len(previously_created_rankers))


def wait_for_training_to_complete(ranker_id):
    """
    Polls (every 30s) the service to check when the ranker's status is no longer "TRAINING".
    Raises exception if the final state is not "AVAILABLE", otherwise returns cleanly.

    :param str ranker_id: the ranker id whose status needs to be checked.
    """
    LOGGER.info("Checking/Waiting for training to complete for ranker %s" % ranker_id)

    response = BLUEMIX_CONNECTION.get_ranker_status(ranker_id=ranker_id)

    while response['status'].upper() == "TRAINING":
        seconds_between_polling_requests = 30
        LOGGER.debug(
                "Ranker still in status: %s. Will continue polling every %d secs." % (
                    response['status'], seconds_between_polling_requests))
        sleep(seconds_between_polling_requests)
        response = BLUEMIX_CONNECTION.get_ranker_status(ranker_id=ranker_id)
        if LOGGER.isEnabledFor(logging.DEBUG):
            print(json.dumps(response, indent=2))

    LOGGER.info("Finished waiting for ranker <<%s>> to train: %s" % (ranker_id, response['status']))

    if response['status'].upper() != "AVAILABLE":
        raise RuntimeError("Unusable ranker, training failed with description: %s" % response['status_description'])


def initialize_logger(log_level):
    """
    Initializes and returns a Logger that prints timestamps and is set to log at the input log level
    :param log_level: level to log messages
    :return: initialized logger
    :rtype: logging.logger
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


def test_ranker(ranker_id, test_file, prediction_outfile):
    """
    Generates runtime requests using the data from the input test file, submits them to the ranker associated with
        the input ranker id and writes returned predictions to the specified output path.  The predictions are in the
        same sequence as the feature vectors in the test file. However, since RaaS only returns top 10 ranked documents
        the remaining document scores are defaulted to -1 (with confidence 0)

    :param str ranker_id: id for the associated ranker in bluemix
    :param file test_file: a csv containing data to use for the requests (question_id, feature_1, feature_2,...,label)
    :param file prediction_outfile: valid path for the prediction file to be created (over writes existing)
    """
    LOGGER.info("Sending runtime requests from <<%s>> to ranker id: <<%s>> (predictions will be written to: <<%s>>)" % (
        test_file, ranker_id, prediction_outfile))

    reader = csv.reader(test_file, delimiter=',')
    feature_names = reader.next()
    feature_names.pop(_QID_COL_INDEX)
    feature_names.pop(_LABEL_COL_INDEX)

    prev_qid = None
    stats = defaultdict(float)

    curr_answer_set = []

    for row in reader:
        if row:
            curr_qid = row[_QID_COL_INDEX]
            if not prev_qid:
                LOGGER.debug("Starting to read answers for the first qid <<%s>>" % curr_qid)
                prev_qid = curr_qid
                curr_answer_set.append(row)

            elif prev_qid != curr_qid:
                LOGGER.debug("We're done reading answers for qid <<%s>>. Generate predictions and prepare to read "
                             "answers for qid <<%s>>" % (prev_qid, curr_qid))

                _update_request_stats(curr_answer_set, stats)
                ranked_candidate_answers = _call_runtime(ranker_id, prev_qid, curr_answer_set, feature_names)
                _update_response_stats(ranked_candidate_answers, stats)
                _write_to_prediction_file(ranked_candidate_answers, prediction_outfile)

                prev_qid = curr_qid
                curr_answer_set = [row]
            else:
                # Keep collecting answers for the current qid
                curr_answer_set.append(row)

    # deal with the last answer set
    if curr_answer_set:
        LOGGER.debug("Generating predictions for the final qid <<%s>>" % prev_qid)

        _update_request_stats(curr_answer_set, stats)
        ranked_candidate_answers = _call_runtime(ranker_id, prev_qid, curr_answer_set, feature_names)
        _update_response_stats(ranked_candidate_answers, stats)
        _write_to_prediction_file(ranked_candidate_answers, prediction_outfile)
    else:
        raise ValueError("No test instances found in the file")

    LOGGER.info("Completed getting runtime predictions for %d questions" % stats['num_questions'])
    # average out the stats across all queries where appropriate
    stats['top-1-accuracy'] = stats['num_top_answers_correct'] / float(stats['num_questions'])
    stats['ndcg@%d' % _TOP_K_FOR_METRICS] /= float(stats['num_questions'])
    stats['recall@%d' % _TOP_K_FOR_METRICS] = float(stats['num_correct_in_top_%d' % _TOP_K_FOR_METRICS]) / stats[
        'num_possible_correct_answers_in_top_%d' % _TOP_K_FOR_METRICS]
    stats['precision@%d' % _TOP_K_FOR_METRICS] /= float(stats['num_questions'])

    return stats


def _write_to_prediction_file(ranked_candidate_answers, outfile):
    """
    Write predictions to the outfile in the desired format and in the natural ordering imposed by the answer id.

    HACK: Assumes that the answer ids were generated in a fashion that maintains the input ordering
    from the test file -- making it easier to run performance calculations using computeAccuracy.pl.

    :param list(CandidateAnswer) ranked_candidate_answers: list of candidate answers with the answer id, rank score
        and confidence score fields populated.
    :param file outfile: open file for writing
    """
    for answer in sorted(ranked_candidate_answers, key=lambda ca: ca.answer_id):
        outfile.write("%.4f %.4f\n" % (answer.rank_score, answer.confidence_score))


def _update_request_stats(candidate_answers, stats):
    stats['num_questions'] += 1
    stats['num_answers_sent_for_ranking'] += len(candidate_answers)


def _compute_precision(rank_ordering, k):
    """
    Helper function to calculate precision at k (i.e. whether or not at least one answer is correct in top k)
    :param list rank_ordering:sequence of ground truth in the rank order returned by the system
    :param int k: top k at which to truncate precision calculation
    :return: 1 if at least one answer was correct in the top k, else 0
    :rtype: numeric
    """
    for r in rank_ordering[0:k]:
        if _is_correct(r):
            return 1
    return 0


def _compute_ndcg(rank_order, ideal_order, k):
    """
    This is a function to get ndcg
    :param list rank_order: sequence of ground truth in the rank order returned by the system
    :param list ideal_order: sequence of ground truth in the ideal order
    :param int k: top k at which to evaluate ndcg
    :return: ndcg for this ordering of ground truth
    :rtype: numeric
    """
    ideal_ndcg = _compute_dcg(ideal_order, k)
    if ideal_ndcg == 0:
        ndcg = 0.0
    else:
        ndcg = _compute_dcg(rank_order, k) / float(ideal_ndcg)
    return ndcg


def _compute_dcg(s, k):
    """
    A function to compute dcg
    :param s: sequence of ground truth in the rank order to use for calculating dcg
    :param k: top k at which to evaluate ndcg
    :return: dcg for this ordering of ground truth
    :rtype: numeric
    """
    dcg = 0.0
    for i in range(min(k, len(s))):
        dcg += (math.pow(2, s[i]) - 1) / math.log(i + 2, 2)
    return dcg


def _update_response_stats(ranked_candidate_answers, stats):
    # Get the ground truth ordering from the candidate answer ranks
    ground_truth_ordering_by_rank = list()
    for answer in ranked_candidate_answers:
        ground_truth_ordering_by_rank.append(answer.ground_truth)
        if answer.rank_score >= 0:
            # HACK: since the service only returns top k answers, we set the score for non-top-k-answers to -1
            stats['num_answers_returned'] += 1

    # Collect stats for precision
    stats['num_top_answers_correct'] += _compute_precision(ground_truth_ordering_by_rank, k=1)
    stats['precision@%d' % _TOP_K_FOR_METRICS] += _compute_precision(ground_truth_ordering_by_rank, k=_TOP_K_FOR_METRICS)

    # Collect stat for ndcg@k
    ideal_ground_truth_ordering = sorted(ground_truth_ordering_by_rank, reverse=True)
    stats['ndcg@%d' % _TOP_K_FOR_METRICS] += _compute_ndcg(ground_truth_ordering_by_rank, ideal_ground_truth_ordering,
                                                           _TOP_K_FOR_METRICS)

    # Collect stats for recall@k
    for i in range(min(_TOP_K_FOR_METRICS, len(ground_truth_ordering_by_rank))):
        if _is_correct(ground_truth_ordering_by_rank[i]):
            stats['num_correct_in_top_%d' % _TOP_K_FOR_METRICS] += 1
        if _is_correct(ideal_ground_truth_ordering[i]):
            stats['num_possible_correct_answers_in_top_%d' % _TOP_K_FOR_METRICS] += 1


def _is_correct(ground_truth_label):
    """
    Returns true if label is > 0, false otherwise
    :param int ground_truth_label:  label
    :return: true or false
    :rtype: bool
    """
    if ground_truth_label > 0:
        return True
    return False


def _call_runtime(ranker_id, qid, candidate_answers, feature_names):
    """
    Helper method for a single runtime request to the specified ranker id for the candidate answers and question id
        provided as input.
    :param str ranker_id: id associated with the ranker to submit the runtime requests to.
    :param str qid: question id associated with the candidate answers
    :param list(CandidateAnswer) candidate_answers: list of feature vectors representing the candidate answers
    :param list(str) feature_names: feature header row
    :return: list of candidate answers some of them have no rank score (these weren't returned by the service)
    :rtype: list(CandidateAnswer)
    """
    mock_answer_id = 0
    gt_lookup = dict()
    for row in candidate_answers:
        # remove the qid and ground truth column and add in an answer id field
        label = row.pop(_LABEL_COL_INDEX)
        if qid != row.pop(_QID_COL_INDEX):
            raise ValueError("Unexpected qid encountered while processing answer set for <<%s>>" % qid)
        mock_answer_id += 1
        row.insert(_ANS_ID_COL_INDEX, mock_answer_id)
        # Keep track of the ground truths since the answers will be re-ordered/pruned by the service
        gt_lookup[mock_answer_id] = int(label)

    answer_file_headers = list(feature_names)
    answer_file_headers.insert(_ANS_ID_COL_INDEX, 'answer_id')

    with tempfile.NamedTemporaryFile() as file_to_send_with_request:
        writer = csv.writer(file_to_send_with_request)
        writer.writerow(answer_file_headers)

        for candidate in candidate_answers:
            writer.writerow(candidate)

        file_to_send_with_request.flush()
        file_to_send_with_request.seek(0)

        num_attempts_for_this_qid = 0
        response = None
        while True:
            try:
                response = BLUEMIX_CONNECTION.rank(ranker_id=ranker_id, answer_data=file_to_send_with_request)
                break
            except WatsonException as ex:
                num_attempts_for_this_qid += 1
                if num_attempts_for_this_qid < _MAX_RUNTIME_ATTEMPTS:
                    LOGGER.warn("Attempt #%d for qid: %s failed. Retrying." % (num_attempts_for_this_qid, qid))
                else:
                    LOGGER.error("Runtime request for qid <<%s>> failed %d time(s) with reason: %s" %
                                 (qid, (num_attempts_for_this_qid + 1), ex.message))
                    raise ex

        if LOGGER.isEnabledFor(logging.DEBUG):
            print(json.dumps(response, indent=2))

        LOGGER.debug("Runtime request processed <<%d>> candidates for qid: <<%s>>" % (
            len(candidate_answers), qid))

        return _parse_candidate_answer_list(qid, gt_lookup, response)


def _parse_candidate_answer_list(qid, gt_lookup, response_contents):
    candidate_answers = list()

    # first collect the answers which were returned by the service
    answers_which_were_returned = list()
    for ranked_answer in response_contents['answers']:
        aid = int(ranked_answer['answer_id'])
        candidate_answers.append(
                CandidateAnswer(qid=qid, answer_id=aid, ground_truth=gt_lookup[aid], rank_score=ranked_answer['score'],
                                confidence_score=ranked_answer['confidence']))
        answers_which_were_returned.append(aid)

    # now deal with the answers which weren't returned
    for aid, gt in gt_lookup.iteritems():
        if aid not in answers_which_were_returned:
            candidate_answers.append(
                    CandidateAnswer(qid=qid, answer_id=aid, ground_truth=gt, rank_score=-1, confidence_score=0))

    return candidate_answers


class CandidateAnswer:
    """
    Class defines a data structure to hold question id, ground truth, rank score, and confidence score for an answer.
    Implements a natural ordering based on answer id
    """

    def __init__(self, qid, answer_id, ground_truth, rank_score=None, confidence_score=None):
        self.qid = qid
        self.answer_id = answer_id
        self.ground_truth = int(ground_truth)
        self.rank_score = float(rank_score)
        self.confidence_score = float(confidence_score)


def validate_mandatory_args(args):
    """
    Checks command line argument sufficiency and raises exception if not met.
    :param args: arguments parsed by the argparse library
    """
    if args.ranker_id is None and args.train_file is None:
        raise ValueError("Either a ranker id should be provided or a training file from which a new ranker will"
                         " be generated.  Found both: <<%s>> and <<%s>>" % (args.ranker_id, args.train_file))
    if args.validation_file is not None and args.outFile is None:
        raise ValueError("Expected valid output location for validation set predictions, but found: <<%s>>" %
                         args.outFile)


def initialize_ranker_connection(credentials_file):
    """
    Initializes and returns a RetrieveAndRankV1 object to use for the experiment based on the credentials
     in the credentials file
    :param File credentials_file:
    :return: RetrieveAndRankV1 object initialized with the provided credentials
    :rtype: RetrieveAndRankV1
    """
    bluemix_url, user, password = parse_credentials(credentials_file)
    return RetrieveAndRankV1(url=bluemix_url, username=user, password=password)


def parse_credentials(config_file):
    """
    Helper returns BLUEMIX_URL, USER, and PASSWORD from the json snippet in the input file
    :param file config_file: file containing the credentials snippet provided by Bluemix UI.  Contents
        should look something like this:
        {
          "credentials": {
            "url": "https://gateway-s.watsonplatform.net/search/api",
            "username": "bb6d90e0-76bc-4454e-b123-32435c724fe6",
            "password": "0sAwXk1Vgrse"
          }
        }
    :return: credentials parsed from the file: BLUEMIX_URL, USER, PASSWORD
    :rtype: tuple(str, str, str)
    """
    try:
        creds = json.load(config_file)['credentials']
        return creds['url'], creds['username'], creds['password']
    except ValueError as ex:
        raise ValueError("Unable to parse creds file <<%s>> as a dictionary of key value pairs: %s" % (
            config_file, ex.message))


def main(args):
    """
    Kicks off training and/or validation set performance evaluation based on the args
    :param args: arguments parsed by the argparse library
    """

    if args.ranker_id:
        ranker_id = args.ranker_id
        wait_for_training_to_complete(ranker_id)
    else:
        ranker_id = train_ranker(train_file=args.train_file, is_enabled_make_space=args.is_enabled_delete_rankers)
        wait_for_training_to_complete(ranker_id)

    if args.validation_file:
        stats = test_ranker(ranker_id, test_file=args.validation_file, prediction_outfile=args.outFile)

        json.dump(stats, args.accuracy_outfile, sort_keys=True, indent=True)


if __name__ == '__main__':
    """
    parses the command line args to setup constants and then calls main runner
    """
    # Get cmd line args
    parser = argparse.ArgumentParser(description='Facilitates learning-to-rank experiments using the /rank API',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', '--train-file', dest='train_file', type=argparse.FileType('rb'),
                        help="Training feature file for ranker in csv format: "
                             "qid,feature_1,feature_2,...,feature_n,ground_truth")
    parser.add_argument('-v', '--validation-file', dest='validation_file', type=argparse.FileType('rb'),
                        help="Validation feature file for testing the Ranker (same format as training file)")
    parser.add_argument('-o', '--output-path', dest='outFile', type=argparse.FileType('wb'),
                        help="Output path for file with rank predictions for validation set")
    parser.add_argument('-a', '--accuracy-output', dest='accuracy_outfile', type=argparse.FileType('wb'),
                        default=sys.stdout, help="output path for accuracy related stats from validation run")
    parser.add_argument('-d', '--debug', help="Print lots of debugging statements", action="store_const",
                        dest="loglevel", const=logging.DEBUG, default=logging.INFO)
    parser.add_argument('-i', '--ranker-id', dest='ranker_id',
                        help="If no training file is specified, this field is required in order to know which"
                             " ranker to use for generating predictions for the validation set.")
    parser.add_argument('-r', '--delete-rankers-if-quota-reached',
                        help="If this flag is enabled, previously created rankers will be deleted if there is "
                             "insufficient space in the user's current quota of rankers to train",
                        action="store_const", dest="is_enabled_delete_rankers", const=True, default=False)
    parser.add_argument('-c', '--credentials-file', dest='bluemix_credentials_file', required=True,
                        type=argparse.FileType('rb'),
                        help="path to file containing bluemix credentials (can be retrieved from the bluemix console. "
                             "Contents will look something like this:"
                             "{\"credentials\": {"
                             "\"url\": \"https://gateway.watsonplatform.net/retrieve-and-rank/api\","
                             "\"username\": \"bb666666-7777-44444-bbbb-333333333333\","
                             "\"password\": \"0sAwXk1Vgrse\"}}")

    args = parser.parse_args()
    validate_mandatory_args(args)

    LOGGER = initialize_logger(args.loglevel)
    BLUEMIX_CONNECTION = initialize_ranker_connection(args.bluemix_credentials_file)

    main(args)