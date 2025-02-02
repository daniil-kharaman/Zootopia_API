import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = 'https://api.api-ninjas.com/v1/animals'
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  params = {
      'name': animal_name
  }
  headers = {
      'X-Api-Key': API_KEY
  }
  response = requests.get(URL, params=params, headers=headers)
  parsed_response = response.json()
  return parsed_response