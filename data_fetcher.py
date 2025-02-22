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
  """

  params = {
      'name': animal_name
  }
  headers = {
      'X-Api-Key': API_KEY
  }
  #added try except
  try:
      response = requests.get(URL, params=params, headers=headers)
      parsed_response = response.json()
      if parsed_response == {'error': 'Missing API Key.'}:
          raise Exception('Missing API Key')
      if parsed_response == {'error': 'name parameter must be provided.'}:
          raise Exception('Missing the parameter "name" in the API request')
      return parsed_response
  except requests.exceptions.MissingSchema:
      print('Impossible to reach the endpoint')
  except Exception as e:
      print(f"Such error occurred: {e}")
