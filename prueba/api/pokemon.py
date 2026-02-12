from fastapi import FastAPI
from schema.pokemon import PokemonModelo
app=FastAPI()

@app.get("/pokemon")
def getPokemon():
    
    return "lista de pokemon"

@app.get("/pokemon/{nombre}")
def getPokemon(nombre):
    return f"info de pokemon {nombre} especifico"

@app.post("/pokemon")
def createPokemon(pokemon:PokemonModelo):
    
    return "pokemon creado"