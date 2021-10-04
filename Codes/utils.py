import requests
import os
import json

def browse(page_num = 0):
  key = os.getenv('NASA_KEY')
  url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page={page_num}'
  return requests.get(url).json()

def feed(start_date, end_date):
  key = os.getenv('NASA_KEY')
  url = f'https://api.nasa.gov/neo/rest/v1/feed?api_key={key}&start_date={start_date}&end_date={end_date}'
  return requests.get(url).json()