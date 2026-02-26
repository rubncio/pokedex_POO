from fastapi import APIRouter, FastAPI
router=APIRouter(prefix="/combates", tags="COMBATE")


@router.post("/")
def createCombate(CombateModel):

    return "combate entre combatientes {combatiente1}{combatiente2}"
