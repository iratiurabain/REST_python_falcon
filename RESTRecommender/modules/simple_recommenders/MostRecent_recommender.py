"""
This is a subclass of MasterRecommender.

It returns the N most recent offers, given a particular state
"""

from modules.simple_recommenders.Master_recommender import MasterRecommender

STATE_JOB_COLUMN = 'State_job'
START_DATE_COLUMN = 'StartDate'
JOBID_COLUMN = 'JobID'

class MostRecentRecommender(MasterRecommender):
    def __init__(self, config):
        super(MostRecentRecommender, self).__init__(config)


    def execute(self, params):
        """ Method that triggers the process """

        data_df = self.read_data.get_all_records_table()

        data_df = self.prepare_data(data_df, params['state_user'])

        # If there are no records, return an empty list
        if data_df.empty:
            return []

        return self.select_offers(data_df, self.config.n_offers)

    def prepare_data(self, data_df, state_user):
        """ Here we prepare the data. In this case we just need to filter and order it """

        return data_df[data_df[STATE_JOB_COLUMN] == state_user].sort_values(by=[START_DATE_COLUMN])

    def select_offers (self,data_df, n_offers):
        """ Here we execute the algorithm we use for predictions.
            In this case we just need to take the first N items
        """

        return list(data_df[JOBID_COLUMN][:n_offers])