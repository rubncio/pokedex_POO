import json
from models.pokemon import Pokemon

def guardarPokemon(pokemon:dict):
    #convertir en dict
    pokemonsJson:list[dict]
    with open("./data/pokemons.json", "r") as pokemons_file:
        pokemonsJson :list[dict]= json.load(pokemons_file)
    with open("./data/pokemons.json", "w") as pokemons_file:
        pokemonsJson.append(pokemon)
        json.dump(pokemonsJson, pokemons_file, indent=4)

def obtenerPokemons():
    with open("./data/pokemons.json", "r") as pokemons_file:
        pokemonsJson :list[dict]= json.load(pokemons_file)
        return pokemonsJson