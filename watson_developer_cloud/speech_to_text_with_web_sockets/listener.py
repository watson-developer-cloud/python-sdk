
class SttListener():
    def __init__(self):
        pass
    """
    This give hypothesis from watson when your sentence is finished
    """
    def listen_hypothesis(self, hypothesis):
        print("Hypothesis: {0}".format(hypothesis))

    """
    This give the json received from watson
    """
    def listen_payload(self, payload):
        print(u"Text message received: {0}".format(payload))
    """
    This give hypothesis from watson when your sentence is not finished
    """
    def listen_interim_hypothesis(self, interimHypothesis):
        print("Interim hypothesis: {0}".format(interimHypothesis))