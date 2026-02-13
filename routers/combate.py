from fastapi import FastAPI
app=FastAPI()


@app.get("/combate/{combatiente1}{combatiente2}")
def getPokemon(combatiente1, combatiente2):

    return "combate entre combatientes {combatiente1}{combatiente2}"
