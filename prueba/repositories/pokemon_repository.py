import json
from pokemon import Pokemon
def guardarPokemon(pokemon:Pokemon):
    
    with open("./data/pokemon.json", "rw") as pokemons_file:
        pokemonsJson :list[dict]= json.load(pokemons_file)
        pokemonsJson
        json.dump(pokemonsJson, pokemons_file, indent=4)