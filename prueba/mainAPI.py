from fastapi import FastAPI
from pokemonAgua import PokemonAgua
from pokemonFuego import PokemonFuego 
app=FastAPI()
#POKEMON
@app.get("/pokemon")
def getPokemon():
    PokemonAgua("pikachu", 100, 100, 100, 75)
    listapokemon=[PokemonAgua("otro", 100, 50, 100, 75), PokemonAgua("pikachu", 100, 100, 100, 75)]
    listaDict=list[dict()]
    for pokemon in listapokemon:
        diccionario={
            "nombre":pokemon.nombre,
            "vida":pokemon.vida,
            "fuerza":pokemon.fuerza,
            "defensa":pokemon.defensa,
            "velocidad":pokemon.velocidad
        }
        listaDict.append
    return 

@app.get("/pokemon/{nombre}")
def getPokemon(nombre):
    return f"info de pokemon {nombre} especifico"

@app.post("/pokemon")
def createPokemon(pokemon):
    
    return "pokemon creado"

#MOVIMIENTOS

@app.get("/movimiento")
def getMovimiento():
    return "lista de pokemon"

@app.get("/pokemon/{nombre}")
def getMovimiento():
    return "info de movimiento especifico"

@app.post("/movimiento")
def createMovimiento(pokemon):
    
    return "movimiento creado"

#COMBATE
@app.get("/combate/{combatiente1}{combatiente2}")
def getPokemon(combatiente1, combatiente2):

    return "combate entre combatientes {combatiente1}{combatiente2}"