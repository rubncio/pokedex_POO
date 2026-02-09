from fastapi import FastAPI
from pikachu import Pikachu
app=FastAPI()

@app.get("/pokemon")
def getPokemon():
    pokemon1=Pikachu(nombre="pikachu", tipo="fuego", nivel=4, vida=150, fuerza=14, defensa=10, velocidad=58
    )
    pokemon2=Pikachu(nombre="pikachuotro", tipo="fuego", nivel=4, vida=150, fuerza=14, defensa=10, velocidad=58
    )
    {
        "pokemon1":pokemon1, 
        "pokemon2":pokemon2
    }
    return "lista de pokemon"

@app.get("/pokemon/{nombre}")
def getPokemon():
    return "info de pokemon especifico"

@app.post("/pokemon")
def createPokemon(pokemon):
    
    return "pokemon creado"