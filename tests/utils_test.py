import requests, json, os, pytest
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('KEY')

def test_feed():
    start_date = '2020-02-01'
    end_date = '2020-02-08'
    url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={key}'
    results = requests.get(url).json()
    keys = list(results)
    assert keys == ['links', 'element_count', 'near_earth_objects']

def test_browse():
    for page_num in range(0, 5):
        url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page={page_num}'
        results = requests.get(url).json()
        keys = list(results)
        assert keys == ['links', 'page', 'near_earth_objects']

def test_lookup():
    astroid_id = 3542519
    url = f'https://api.nasa.gov/neo/rest/v1/neo/{astroid_id}?api_key={key}'
    results = requests.get(url).json()
    keys = list(results)
    assert keys == ['links', 'id', 'neo_reference_id', 'name', 'designation',\
        'nasa_jpl_url', 'absolute_magnitude_h', 'estimated_diameter', \
        'is_potentially_hazardous_asteroid', 'close_approach_data', \
        'orbital_data', 'is_sentry_object']