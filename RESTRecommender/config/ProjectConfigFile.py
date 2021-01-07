"""
This class reads all the init configuration variables from the configuration file (either local or prod) and
initializes the logger

"""
import logging
from configparser import ConfigParser

from resources.patterns.Singleton import Singleton


class ProjectConfigFile(object, metaclass=Singleton):
    def __init__(self, path):

        # Load Configuration file and read variables
        parser = ConfigParser()
        parser.read(path)

        # Initialize logger
        log_level_name = parser.get('logger', 'log_level')
        log_level = logging.getLevelName(log_level_name)
        logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.getLogger('sqlalchemy.engine').setLevel(log_level)

        # Read the paths
        self.path_jobs= parser.get('data_paths', 'path_jobs')
        self.path_users = parser.get('data_paths', 'path_users')
        self.path_app_int = parser.get('data_paths', 'path_app_int')

        # Simple recommender
        self.n_offers = int(parser.get('simple_recommender', 'n_offers'))


        logging.info('Finished reading configuration file')
