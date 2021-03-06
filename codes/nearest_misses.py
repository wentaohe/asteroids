import json
from .asteroid_closest_approach import asteroid_closest_approach

def nearest_misses():
    
    #taking care of the API limit, setting a page limit to 5
    #asteroids = json.loads(asteroid_closest_approach(page_limit))
    asteroids = json.loads(asteroid_closest_approach(5))
    asteroids_sorted = sorted(asteroids, key=lambda x:x['close_approach_data']['miss_distance']['astronomical'])
    nearests = asteroids_sorted[0:10]

    return json.dumps(nearests)