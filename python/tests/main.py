import requests 

URL ='https://api.pokemonbattle.ru/v2'
TOKEN ='7bbb7580e1ad8e51240e7adbfce01d6f'
HEADER ={'Content-Type':'application/json','trainer_token': TOKEN}

POKEMON_ID =  '169208'

body_registration = {
    "trainer_token": TOKEN,
    "email": "",
    "password": ""
}

body_confirmation ={
    "trainer_token": TOKEN
}

'''body_create ={
    "name": "Бульбазавр",
    "photo_id": 1
}
'''

body_change = {
    "pokemon_id": POKEMON_ID,
    "name": "Пупун",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": POKEMON_ID 
}

'''response = requests.post(url = f'{URL}/trainers/reg',headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email',headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''message = response_create.json () ['message']
print(message)'''

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.json)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.json)