import sklearn
from sklearn.model_selection import train_test_split
import pandas as pd


def split_data(X):
    """
    Imports proper sklearn module and splits a dataframe into test and validation 
    dataframes. (must have sklearn installed)
    
    Returns datafrmaes 'train' & 'val'

    Params:

        X = a pandas dataframe to be split

    Example: train, val = split_data(df)
    """
    train, val = train_test_split(X, random_state=42)
    return train, val

class Feature(object):
    def __init__(self, feature, target):
        self.internal_feature = feature
        self.internal_target = target

    @property
    def maximum(self):
        return self.internal_feature.max()

    @property
    def minimum(self):
        return self.internal_feature.min()

    @property
    def correllation(self):
        return self.internal_feature.corr(self.internal_target)  