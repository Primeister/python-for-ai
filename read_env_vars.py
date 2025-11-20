import os
from dotenv import load_dotenv

#put path in parantheses
load_dotenv(".env")

api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE')

print(f"api key: {api_key}")