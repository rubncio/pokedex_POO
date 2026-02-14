from fastapi import APIRouter, FastAPI, HTTPException
from schema.pokemon import PokemonModelo
from controller.pokemon_controller import crearPokemon, consultarPokemon

router=APIRouter(prefix="/pokemon", tags="POKEMON")

@router.get("/")
def getPokemon():
    #obtenerPokemons()
    return "lista de pokemon"

@router.get("/{nombre}")
def getPokemon(nombre):
    pokemon=consultarPokemon(nombre)
    if not pokemon:
        raise HTTPException(404,"pokemon no encontrado")
    return pokemon.toDict()

@router.post("/")
def createPokemon(pokemon:PokemonModelo):
    crearPokemon(pokemon)
    return "pokemon creado"