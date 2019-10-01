"""
utility functions for working with DataFrames
"""

import pandas

TEST_DF = pandas.DataFrame([1,2,3])

def boxplot(x,y,dataframe):
    import matplotlib.pyplot as plt
    %matplotlib inline
    return dataframe.boxplot(column="y",by="x")


# Function for creating any time range
def Prior_Period_YoY_Change(df_column, prior_period_length=1):

    numerator = 0
    for i in range(prior_period_length + 1):
        numerator += df_column.shift(-i)

    denominator = 0
    for i in range(prior_period_length + 1):
        denominator += df_column.shift(-i - 12)

    return (1 - (numerator / denominator)) 
