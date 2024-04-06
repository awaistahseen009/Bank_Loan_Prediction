from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
'''
NUMERICAL COLUMNS IMPUTING
Lets impute the values by median values because mean is effected by extreme values
We can use sklearn imputer but lets do it manually
'''
class MedianImputer(BaseEstimator, TransformerMixin):
    def __init__(self, cols):
        self.cols = cols
    def fit(self, X, y=None): # y is optional
        self.med_dict = dict()
        for col in self.cols :
            self.med_dict[col] = X[col].median()
        return self
    
    def transform(self, X ):
        X = X.copy() # Creating the deep copy
        for col in self.cols:
            X[col].fillna(self.med_dict[col], inplace=True)
        return X
    


'''
CATEGORICAL COLUMNS IMPUTING
Lets impute the values by mode values which means mostly occuring
'''
class ModeImputer(BaseEstimator, TransformerMixin):
    def __init__(self, cols):
        self.cols = cols
    def fit(self, X, y=None): # y is optional
        self.mode_dict = dict()
        for col in self.cols :
            self.mode_dict[col] = X[col].mode()[0]
        return self
    
    def transform(self, X ):
        X = X.copy() # Creating the deep copy
        for col in self.cols:
            X[col].fillna(self.mode_dict[col], inplace=True)
        return X


class SqrtTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, cols):
        self.cols = cols
    def fit(self, X, y=None): # y is optional
        return self
    
    def transform(self, X ):
        X = X.copy() # Creating the deep copy
        for col in self.cols:
            X[col] = np.sqrt(X[col])
        return X
    

# We can also use the label encoder but lets implement it manually
class EncodeCategoricalColumns(BaseEstimator, TransformerMixin):
    def __init__(self , cols):
        self.cols = cols
    def fit(self, X, y=None) :
        return self
    def transform(self , X):
        for col in self.cols:
            for i , value in enumerate(X[col].unique()):
                X[col] = X[col].replace({value: i})
        return X
    

class DropFeatures(BaseEstimator, TransformerMixin):
    def __init__(self , cols):
        self.cols = cols
    def fit(self, X, y=None) :
        return self
    def transform(self , X):
        X = X.drop(self.cols, axis=1)
        return X
    