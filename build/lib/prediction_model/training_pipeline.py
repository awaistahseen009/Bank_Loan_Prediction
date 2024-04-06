import pandas as pd
import sys
import numpy as np
from prediction_model.processing.data_handling import load_dataset, save_model_pipeline 
import prediction_model.processing.preprocessing as pp
from prediction_model.config import config

import prediction_model.pipeline as pipe
def train():
    X = load_dataset(config.TRAIN_FILE)
    y = X[config.TARGET].map({'N':0, 'Y':1})
    pipe.pipe.fit(X[config.FEATURES], y)
    save_model_pipeline(pipe.pipe)


if __name__ == "__main__":
    train()