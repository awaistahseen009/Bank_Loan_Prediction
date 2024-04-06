from sklearn.pipeline import Pipeline
from prediction_model.config import config
import prediction_model.processing.preprocessing as pp
from sklearn.ensemble import BaggingClassifier
from sklearn.preprocessing import MinMaxScaler
import numpy as np
pipe = Pipeline(
    [
        ('Median Imputation', pp.MedianImputer(cols=config.NUM_COL)),
        ('Mode Imputation', pp.ModeImputer(cols=config.CAT_COL)),
        ('Dropping Features', pp.DropFeatures(cols=config.FEATURES_TO_DROP)),
        ('Categorical Encoding',pp.EncodeCategoricalColumns(cols=config.CAT_COL)),
        ('Feature Square Root (Normalizing)',pp.SqrtTransformer(cols=config.SQRT_FEATURES)),
        ('Min Max Scaling',MinMaxScaler()),
        ('Bagging Classifier',BaggingClassifier(n_estimators=100, random_state=2))
    ]
)