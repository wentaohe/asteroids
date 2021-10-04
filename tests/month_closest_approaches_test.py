import requests, json, os, pytest, sys
from codes.month_closest_approaches import month_cloest_approaches
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('KEY')

def test_month_cloest_approaches():
    month_data = month_cloest_approaches('2018-02')
    results = json.loads(month_data)

    #test cases
    #assert list(results) == ['month', 'element_count', 'near_earth_objects']
    assert results['month'] == '2018-02'