import requests, json, os, pytest, sys
from codes.asteroid_closest_approach import asteroid_closest_approach
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('KEY')

def test_asteroid_closest_approach():
    asteroids_data = asteroid_closest_approach()
    asteroids = json.loads(asteroids_data)

    #test cases
    #assert asteroids[0]['links']
    assert float(asteroids[0]['close_approach_data']['miss_distance']['astronomical'])