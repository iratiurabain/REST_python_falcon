"""
Initial script for start listening for REST webservice

"""

import sys
import falcon

sys.path.append('modules/simple_recommenders')
sys.path.append('REST')

from REST.RecommenderREST import RecommenderREST

# Listen on the following routes:
recommender_app = api = falcon.API()
api.add_route('/recommender', RecommenderREST())
