import json
import math
from .utils import feed, browse, lookup

def asteroid_closest_approach(page_limit = None):
    asteroids = []
    browse_data = browse()
    