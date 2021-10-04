import json
import math
from .utils import feed, browse, lookup

def asteroid_closest_approach(page_limit = None):
    closest_asteroids = []
    browse_data = browse() 
    number_of_pages = browse_data['page']['total_pages']

    #to take care of the API limit
    #for page in range(0, number_of_pages):
    for page in range(0, 5):
        asteroids = browse(page)
        results = find(asteroids, closest_asteroids)
    return json.dumps(results)

def find(asteroids, closest_asteroids):
    for asteroid in asteroids['near_earth_objects']:
        if asteroid['close_approach_data']:
            asteroid['close_approach_data'] = min(asteroid['close_approach_data'], key=lambda x:x['miss_distance']['astronomical'])
            closest_asteroids.append(asteroid)
    return closest_asteroids
