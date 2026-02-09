from fastapi import FastAPI
app=FastAPI()


@app.get("/combate/{combatiente1}{combatiente2}")
def getPokemon(Combatiente1, combatiente2):

    return "info de pokemon especifico"
