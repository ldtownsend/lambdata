"""
Utility functions for working with the Energy Information Agency's dataset
"""

import pandas as pd
import numpy as np

class Datetimes:

    def __init__(self, data):
        """
        takes in a DataFrame
        """
        self.data = data

    def to_datetime(self, time_feats):
        """
        df is the DataFrame
        time_feats is a list of the features to be changed to datetime format
        """
        for col in self.data:
            if col in time_feats:
                self.data[col] = pd.to_datatime(self.data[col])


    def dt_differences(self, dt_dif_name, dt1, dt2):
        """
        dt_dif_name enter a string for the name of the new feature
        dt1 is the datetime feature you want to treat as the starting point
        dt2 is the datetime feature you want to treat as the ending point
        """
        df1 = self.data.copy()
        df1[dt_dif_name] = df1[dt1] - df1[dt2]
        return df1[dt_dif_name]



class Project_Energy:

    def Prior_Period_YoY_Change(df_column, prior_period_length=1):
        """
        A calculation for finding the year-over-year growth for some feature,
        over a certain period length, in a dataset with monthly frequency.
        """
        numerator = 0
        for i in range(prior_period_length + 1):
            numerator += df_column.shift(-i)

        denominator = 0
        for i in range(prior_period_length + 1):
            denominator += df_column.shift(-i - 12)

        return (1 - (numerator / denominator))
