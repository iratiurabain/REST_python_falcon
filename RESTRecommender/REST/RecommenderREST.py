"""
Class to handle GET and POST requests
"""
import json
import logging
import time
import sys

import falcon
from modules.simple_recommenders.MostRecent_recommender import MostRecentRecommender
from config.ProjectConfigFile import ProjectConfigFile

class RecommenderREST(object):
    """ Falcon REST compliant class
    """

    def __init__(self):
        self.config = ProjectConfigFile('resources/config/config-local.ini' if len(sys.argv) < 2 else sys.argv[1])
        self.most_recent_recommender = MostRecentRecommender(self.config)

    def on_get(self, req, resp):
        """ On get request, call the simple recommender and return the result
        """
        self.build_response(req, resp)

    def build_response(self, req, resp):

        try:
            ts = time.time()

            # Read input parameters
            request_body = json.load(req.bounded_stream)
            state_user = request_body['state_user']

            # Execute the recommender
            list_offers = self.most_recent_recommender.execute({"state_user": state_user})

            # Calculate execution time in seconds
            te = time.time()

            result = {
                "id": 1,
                "type": "recommendation",
                "user_id": request_body['user_id'],
                "job_ids": list_offers,
                "application_ts": te - ts   # Return execution time
            }

            # Return the result in json format
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(result)

        except Exception as e:
            logging.error(e)
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({})

    def on_post(self, req, resp):
        """ On post request call get
        """
        self.on_get(req, resp)
