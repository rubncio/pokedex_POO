from api.schema.pokemon import PokemonModelo
from pokemon import Pokemon
from repositories.pokemon_repository import *
def crearPokemon(pokemonModel:PokemonModelo):
    pokemon =Pokemon(pokemonModel.nombre,
        pokemonModel.vida,
        pokemonModel.fuerza,
        pokemonModel.defensa,
        pokemonModel.velocidad,
        pokemonModel.tipo)
    guardarPokemon(pokemon)

def consultarPokemon(nombre):
    pokemons_dict=obtenerPokemons()
    pokemon:Pokemon
    for pokemond in pokemons_dict:
        if pokemond.get("nombre")==nombre:
            pokemon=Pokemon.fromDict(pokemond)
    return pokemon
    