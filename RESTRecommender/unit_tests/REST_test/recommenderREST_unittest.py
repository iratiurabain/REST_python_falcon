"""
UNIT tests.

This is just an example unit test. We need to try to have as much coverage as possible (ideally > 80-90%), and for this the unit tests
need to go through as many code lines as possible.

Other unit test that we would need to write:

- Other tests that we can do:
    * Test whether the REST can handle bad requests (eg., errors in the json)
    * test whether the REST can handle bad input parameters (eg., a country that doesn't exists)
    * Test that the application can read the data (no files, or empty files)
    * Test that the join table was done correctly (test it calculating the expected dimension)
    * Test that the data format from the datafile is the one we expect (the columns that we need exist).
    * Test that given an array of synthetic data, the recommender displays the N most recent items.
    * Test that chanching the n_offers (number of offers we want the algorithm to return) works.


"""
import time
import types
from unittest import TestCase
from unittest.mock import MagicMock
from collections import namedtuple


from REST.RecommenderREST import RecommenderREST

Req = namedtuple('Req', ['content_length', 'bounded_stream'])


class TestRecommenderREST(RecommenderREST):
    def __init__(self):
        self.config = MagicMock()
        self.most_recent_recommender = MagicMock()


class TestRecommenderRest(TestCase):


    def test_legal_request(self):
        """ This test evaluates that the response is built correctly ."""
        recommender_rest = TestRecommenderREST()

        time.time = MagicMock(return_value=1)

        req = MagicMock()
        req.content_length = 100
        req.bounded_stream = MagicMock()
        req.bounded_stream.read = MagicMock(
            return_value='{"type": "recommendation","user_id": 1,"state_user":"FL","timestamp" : 0}')

        req.get_param = MagicMock(return_value='1')
        resp = types.SimpleNamespace()

        recommender_rest.most_recent_recommender.execute = MagicMock(
            return_value=[1,2,3,4,5])
        recommender_rest.build_response(req, resp)

        self.assertEqual(resp.body,
                         '{"id": 1, "type": "recommendation", "user_id": 1, "job_ids": [1, 2, 3, 4, 5], "application_ts": 0}')
        self.assertEqual(resp.status, '200 OK', "Unexpected status response in legal request")