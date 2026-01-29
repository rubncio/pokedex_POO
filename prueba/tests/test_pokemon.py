import pytest
from pokemon import Pokemon
from exceptions.oponenteVacio import OponenteVacio
pokemon=Pokemon(nombre="pikachu", tipo="fuego", nivel=4, vida=150, fuerza=14, defensa=10, velocidad=58, movimientos=[Movimiento("fuego",33),Movimiento("agua",95),Movimiento("naturaleza",41),Movimiento("magia",50)]
    )
def ejecutarMovimientoOponenteVacio():
    with pytest.raises(OponenteVacio):
        pokemon.ejecutar_movimiento()

def recibirDaño():
