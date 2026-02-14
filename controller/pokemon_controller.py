from schema.pokemon import PokemonModelo
from models.pokemon import Pokemon
from repositories.pokemon_repository import *
from exceptions.recursoYaExistenteException import RecursoYaExistenteException

def crearPokemon(pokemonModel:PokemonModelo):
    if consultarPokemon(pokemonModel.nombre):
        raise RecursoYaExistenteException("pokemon")
    pokemon =Pokemon(pokemonModel.nombre,
        pokemonModel.vida,
        pokemonModel.fuerza,
        pokemonModel.defensa,
        pokemonModel.velocidad,
        pokemonModel.tipo)
    guardarPokemon(pokemon.toDict())
    
        

def consultarPokemon(nombre):
    #itera la lista de dict, siendo cada uno blabla y si hay alguno que coincida con nombre se guardara en pokemon si no None.
    pokemon=next([pokemond for pokemond in obtenerPokemons() if pokemond.get("nombre")==nombre], None)
    return pokemon
    