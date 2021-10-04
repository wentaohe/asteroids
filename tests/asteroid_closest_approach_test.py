import requests, json, os, pytest
from codes.asteroid_closest_approach import asteroid_closest_approach
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('KEY')

