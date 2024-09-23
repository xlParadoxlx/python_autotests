import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '16e21167f4aa7ff9471dfb04660c82c8'
HEADER = {'Content-Type' : 'application/json', "trainer_token": TOKEN}
TRAINER_ID = '6384'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == "6384"