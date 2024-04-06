import pathlib
import prediction_model
import os
PAKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent
DATASETS = os.path.join(PAKAGE_ROOT, 'datasets')
TRAIN_FILE = 'train.txt'
TEST_FILE = 'test.txt'
TARGET = 'Loan_Status'
MODEL_NAME = 'model.pkl'
SAVE_MODEL = os.path.join(PAKAGE_ROOT, 'trained_models')

SAVE_MODEL_PATH = os.path.join(os.path.join(PAKAGE_ROOT, 'trained_models'), MODEL_NAME)
FEATURES = [ 'Loan_ID','Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']
NUM_COL = ['ApplicantIncome',
 'CoapplicantIncome',
 'LoanAmount',
 'Loan_Amount_Term']
CAT_COL = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area','Credit_History']

FEATURES_TO_DROP = ['Loan_ID']

SQRT_FEATURES = ['ApplicantIncome', 'CoapplicantIncome','LoanAmount']