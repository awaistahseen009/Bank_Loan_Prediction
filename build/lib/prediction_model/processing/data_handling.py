import pandas as pd
import numpy as np
import numpy as np
import joblib
import os
from prediction_model.config import config

def load_dataset(path:str)->pd.DataFrame:
    file_path = os.path.join(config.DATASETS, path)
    _data = pd.read_csv(file_path)
    return _data

def save_model_pipeline(model_pipeline):
    save_path = os.path.join(config.SAVE_MODEL, config.MODEL_NAME)
    joblib.dump(model_pipeline, save_path)
    print(f"Model has been saved successfully with name: {config.MODEL_NAME} under directory {save_path}")

def load_model_pipeline(model_pipeline):
    model = joblib.load(model_pipeline)
    return model