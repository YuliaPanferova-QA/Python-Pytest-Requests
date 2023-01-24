import requests


token = '1a0ef0a5d475e9b7102c253688e7b8b3'


response = requests.post('https://pokemonbattle.me:5000/pokemons',headers= {'Content-Type': 'application/json', 'trainer_token':token},
   json= 
    {
    "name": "Магнолия",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response.text)

response_confirm = requests.put('https://pokemonbattle.me:5000/pokemons',headers= {'Content-Type': 'application/json', 'trainer_token':token},
   json= 
  {
    "pokemon_id": 3254,
    "name": "Роза",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response_confirm.text)

response_confirm = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',headers= {'Content-Type': 'application/json', 'trainer_token':token},
   json= 
  {
    "pokemon_id": "3254"
})

print(response_confirm.text)
