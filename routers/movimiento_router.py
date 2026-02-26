from fastapi import APIRouter, FastAPI
router=APIRouter(prefix="/movimientos", tags="MOVIMIENTO")

@router.get("/")
def getMovimiento():
    return "lista de pokemon"

@router.get("/{nombre}")
def getMovimiento(nombre):
    return "info de movimiento especifico"

@router.post("/")
def createMovimiento(movimiento:MovimientoModelo):
    
    return "movimiento creado"

@router.put("/{nombre}}")
def modifyMovimiento(nombre, movimiento:MovimientoModelo):
    
    return "movimiento modificado"

@router.delete("/{nombre}}")
def deleteMovimiento(nombre):
    
    return "movimiento eliminado"