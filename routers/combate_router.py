from fastapi import APIRouter, FastAPI
router=APIRouter(prefix="/combate", tags="COMBATE")


@router.get("/{combatiente1}{combatiente2}")
def getPokemon(combatiente1, combatiente2):

    return "combate entre combatientes {combatiente1}{combatiente2}"
