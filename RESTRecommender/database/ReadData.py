"""
This class reads the data files.

"""

from resources.patterns.Singleton import Singleton
import pandas as pd

class ReadData(object, metaclass=Singleton):

    def __init__(self, path_jobs, path_users, path_app_int):

        self.jobs_df = pd.read_csv(path_jobs)
        self.users_df = pd.read_csv(path_users)
        self.app_int_df = pd.read_csv(path_app_int)

        # Join the tables
        self.users_join_df = self.users_df.merge(self.app_int_df, how='left', left_on='UserID', right_on='UserID')
        self.all_records_df = self.users_join_df.merge(self.jobs_df, how='outer', left_on='JobID', right_on='JobID',
                                             suffixes=('_user', '_job'))

    def get_all_records_table(self):

        return self.all_records_df


