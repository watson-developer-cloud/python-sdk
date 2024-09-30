import unittest, json
from examples.URL_nlu_t2s import app


class TestApp(unittest.TestCase):
    """
    Test cases on the Flask application for checking correctness, functionality
    """
    def setUp(self):
        """ Set up the test environment """
        # Initialize the Flask application
        self.app = app.test_client()   # open a flask API test client
        self.app.testing = True

    def test_valid_data(self):
        response = self.app.post('/',
                                data='{"url": "https://github.com/jkd2021/audience-segment-match-api", "keywords_num": 5}',
                                content_type='application/json'
                                )
        data = json.loads(response.data)
        print(data)


if __name__ == '__main__':
    unittest.main()