import requests, json, os, pytest, sys
from codes.nearest_misses import nearest_misses
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('KEY')

def test_nearest_misses():
    misses = nearest_misses()
    results = json.loads(misses)
    for x in range(0, 9):
        current = results[x]['close_approach_data']['miss_distance']['astronomical']
        next = results[x + 1]['close_approach_data']['miss_distance']['astronomical']

        #test cases
        assert current <= next
    
    assert len(results) == 10
