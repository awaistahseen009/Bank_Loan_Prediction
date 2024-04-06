import pandas as pd
import numpy as np
from prediction_model.processing.data_handling import load_model_pipeline, load_dataset
import joblib
from prediction_model.config import config

pipeline = load_model_pipeline(config.SAVE_MODEL_PATH)

def generate_predictions(dataset):
    df = pd.DataFrame(dataset) 
    pred = pipeline.predict(df[config.FEATURES])
    out = np.where(pred == 1,'Y','N')
    return {'Predictions':out}

# def generate_predictions():
#     df = load_dataset(config.TEST_FILE)
#     pred = pipeline.predict(df[config.FEATURES])
#     out = np.where(pred == 1,'Y','N')
#     return {'Predictions':out}

if __name__  == '__main__':
    generate_predictions()