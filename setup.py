from setuptools import  setup , find_packages
import os
import io
from pathlib import Path
NAME = "prediction_model"
DESCRIPTION = 'Bank Loan Status Prediction'
VERSION = "1.0.0"
URL = "https://github.com/awaistahseen009/"
EMAIL = "awaistahseenaccoun@gmail.com"
AUTHOR = "Awais Tahseen"
REQUIRES_PYTHON = ">=3.7.0"
pwd = os.path.abspath(os.path.dirname(__file__))
def list_req(filename = "requirements.txt"):
    with io.open(os.path.join(pwd, filename), encoding='utf-8') as f:
        return f.read().splitlines()

try :
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_desc =  "\n" + f.read()
except  FileNotFoundError:
    long_desc = DESCRIPTION

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR/"VERSION") as f:
    _version = f.read().strip()
    about["version"] = _version


setup(
    name=NAME,
    version=about["version"],
    description=DESCRIPTION,
    long_description=long_desc,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'prediction_model': ['VERSION', 'datasets/*.txt']},
    install_requires = list_req(),
    extras_require = {},
    include_package_data= True,
    license='MIT',
    classifiers=[
        'LICENSE :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
