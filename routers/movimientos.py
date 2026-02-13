from fastapi import FastAPI
app=FastAPI()

@app.get("/movimiento")
def getMovimiento():
    return "lista de pokemon"

@app.get("/pokemon/{nombre}")
def getMovimiento():
    return "info de movimiento especifico"

@app.post("/movimiento")
def createMovimiento(pokemon):
    
    return "movimiento creado"