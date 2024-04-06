import pytest
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

'''
We will be performing the following tests
1. Input has length of columns defined in FEATURES
2. Ouput is not NULL
3. Output should be a dictionary
4. Output should be a str instance
'''
@pytest.fixture 
def predict():
    input_value = load_dataset(config.TEST_FILE)[:1]
    results = generate_predictions(input_value)
    return results, input_value

def test_input_values(predict):
    _ , input_value = predict
    assert len(input_value.columns) == len(config.FEATURES)

def test_output_NULL(predict):
    result, _ = predict
    assert result is not None

def test_output_dict(predict):
    result , _  = predict
    assert isinstance(result,dict)

def test_output_pred_str(predict):
    result , _ = predict
    assert isinstance(result.get('Predictions')[0], str)