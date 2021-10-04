import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

def feed(start_date, end_date):
  key = os.getenv('KEY')
  url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={key}'
  return requests.get(url).json()

def browse(page_num = 0):
  key = os.getenv('KEY')
  url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page={page_num}'
  return requests.get(url).json()

def lookup(astroid_id):
  key = os.getenv('KEY')
  url = f'https://api.nasa.gov/neo/rest/v1/neo/{astroid_id}?api_key={key}'
  return requests.get(url).json()

results = browse(1)
print(list(results))