"""
Master recommender.

Here we would add all the things that are common for all recommender algorithms.

"""
import abc
from database.ReadData import ReadData


class MasterRecommender(object):
    def __init__(self, config):
        self.config = config

        self.read_data = ReadData(self.config.path_jobs,
                                  self.config.path_users,
                                  self.config.path_app_int)

    @abc.abstractmethod
    def execute(self, params):
        return