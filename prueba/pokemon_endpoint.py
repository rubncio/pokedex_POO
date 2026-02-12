from fastapi import FastAPI, HTTPException
from api.schema.pokemon import PokemonModelo
from service.pokemon_service import crearPokemon, consultarPokemon
app=FastAPI()

@app.get("/pokemon")
def getPokemon():
    #obtenerPokemons()
    return "lista de pokemon"

@app.get("/pokemon/{nombre}")
def getPokemon(nombre):
    pokemon=consultarPokemon(nombre)
    if not pokemon:
        raise HTTPException(404,"pokemon no encontrado")
    return pokemon.toDict()

@app.post("/pokemon")
def createPokemon(pokemon:PokemonModelo):
    crearPokemon(pokemon)
    return "pokemon creado"