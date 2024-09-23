import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '16e21167f4aa7ff9471dfb04660c82c8'
HEADER = {'Content-Type' : 'application/json', "trainer_token": TOKEN}


body_create_pok = {
    "name": "generate",
    "photo_id": -1
}
body_change_name = {
    "pokemon_id": "73791",
    "name": "BubaBuba",
    "photo_id": -1
}
body_add_pokeball = {
    "pokemon_id": "73791"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pok)
print(response_create.text)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

pokemon_id = response_create.json['id']