from fastapi import FastAPI
from api.schema.pokemon import PokemonModelo
from service.pokemon_service import crearPokemon
app=FastAPI()

@app.get("/pokemon")
def getPokemon():
    
    return "lista de pokemon"

@app.get("/pokemon/{nombre}")
def getPokemon(nombre):
    return f"info de pokemon {nombre} especifico"

@app.post("/pokemon")
def createPokemon(pokemon:PokemonModelo):
    crearPokemon(pokemon)
    return "pokemon creado"