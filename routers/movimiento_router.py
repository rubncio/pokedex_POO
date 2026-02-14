from fastapi import APIRouter, FastAPI
router=APIRouter(prefix="/movimiento", tags="MOVIMIENTO")

@router.get("/")
def getMovimiento():
    return "lista de pokemon"

@router.get("/{nombre}")
def getMovimiento():
    return "info de movimiento especifico"

@router.post("/movimiento")
def createMovimiento(pokemon):
    
    return "movimiento creado"