import requests 
import pytest

URL ='https://api.pokemonbattle.ru/v2'
TOKEN =''
HEADER ={'Content-Type':'application/json','trainer_token': TOKEN}
TRAINER_ID = ''

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons',params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
        response_get = requests.get(url = f'{URL}/pokemons',params = {'trainer_id': TRAINER_ID})
        assert response_get.json()["data"][0]['name'] == 'Бульбазавр'


@pytest.mark.parametrize('key,value',[('name','Бульбазавр'),('trainer_id', TRAINER_ID),('trainer_id', '23231')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons',params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value



def test_get_trainers():
    url = "https://pokemonbattle.ru/"
    response = requests.get(url + "trainers")
    assert response.status_code == 200

  






