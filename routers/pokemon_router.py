from fastapi import APIRouter, FastAPI, HTTPException
from schema.pokemon import PokemonModelo
from schema.setmovimientos import SetMovimientos
from controller.pokemon_controller import crearPokemon, consultarPokemon
from models.pokemon import Pokemon

router=APIRouter(prefix="/pokemones", tags="POKEMON")

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

@router.put("/{nombre}")
def modifyPokemon(nombre, pokemon:PokemonModelo):

    return "pokemon modificado"

@router.delete("/{nombre}")
def createPokemon(nombre):
    
    return "pokemon eliminado"

@router.post("/{nombre}/movimientos")
def asignarMovimientos(nombre,movimientos:SetMovimientos):
    # pokemon=consultarPokemon(nombre)
    # if not pokemon:
    #     raise HTTPException(404,"pokemon no encontrado")
    # Pokemon.fromDict(pokemon).movimientos(movimientos.l)
    return f"movimiento/s asignados al pokemon {nombre}"
    