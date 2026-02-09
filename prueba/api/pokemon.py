from fastapi import FastAPI
from main import getpokemon
app=FastAPI()

@app.get("/pokemon")
def getPokemon():
    
    return getpokemon()

@app.get("/pokemon/{nombre}")
def getPokemon():
    return "info de pokemon especifico"

@app.post("/pokemon")
def createPokemon(pokemon):
    
    return "pokemon creado"