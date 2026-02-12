from pydantic import BaseModel


class PokemonModelo(BaseModel):
    nombre:str
    vida:str
    fuerza:str
    defensa:str
    velocidad:str
    tipo:str