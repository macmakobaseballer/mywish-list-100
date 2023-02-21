import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = '../.env'

load_dotenv(dotenv_path)

DYN_ENDPOINT_URL = os.environ.get('DYN_ENDPOINT_URL')
DYN_REGION_NAME = os.environ.get('DYN_REGION_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') 

