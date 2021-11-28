import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv('API_KEY')
api_secret=os.getenv('API_SECRET')
access_token=os.getenv('ACCESS_TOKEN')
access_secret=os.getenv('ACCESS_SECRET')
num_dm=os.getenv('NUM_DM')
keyword=os.getenv('KEYWORD')
text_length=int(os.getenv('TEXT_LENGTH'))
time_sleep=int(os.getenv('TIME_SLEEP'))
add_time_sleep=int(os.getenv('ADD_TIME_SLEEP'))
