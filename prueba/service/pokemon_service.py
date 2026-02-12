from api.schema.pokemon import PokemonModelo
from pokemon import Pokemon
from repositories import pokemon_repository
def crearPokemon(pokemonModel:PokemonModelo):
    pokemon =Pokemon(pokemonModel.nombre,
        pokemonModel.vida,
        pokemonModel.fuerza,
        pokemonModel.defensa,
        pokemonModel.velocidad,
        pokemonModel.tipo)
    pokemon_repository.guardarPokemon(pokemon)
    