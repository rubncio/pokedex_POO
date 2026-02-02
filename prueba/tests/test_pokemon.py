import pytest
from pokemon import Pokemon
from movimiento import Movimiento
from exceptions.oponenteVacio import OponenteVacio

pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58)

def ejecutarMovimientoOponenteVacio():
    with pytest.raises(OponenteVacio):
        pokemon.ejecutar_movimiento()

def setMovimientoIncompatible():
    movimientoAgua=Movimiento("chorro", 95, "agua")
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58, movimientos=[movimientoAgua, movimientoAgua, movimientoAgua, movimientoAgua])
    
    with pytest.raises(TypeError):
        
        pokemon.movimientos=movimientoAgua

def setMovimientoCompatible():
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58)
    movimientoFuego=Movimiento("achicharramiento", "fuego", 95)
    pokemon.setMovimiento(movimientoFuego)
    assert len(pokemon.getMovimientos()) == 1

def setMovimientoMasDeCuatroError():
    movimientoAgua=Movimiento("chorro", 95, "agua")
    pokemon=Pokemon(nombre="pikachu", tipo="agua", vida=150, fuerza=14, defensa=10, velocidad=58, movimientos=[movimientoAgua, movimientoAgua, movimientoAgua, movimientoAgua])
    
    with pytest.raises(IndexError):
        pokemon.movimientos=movimientoAgua
    
def setMovimientoMasDeCuatroBien():
    movimientoFuego=Movimiento("llamarada", 95, "fuego")
    movimientoAgua=Movimiento("chorro", 95, "agua")
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58, movimientos=[movimientoFuego, movimientoFuego, movimientoFuego, movimientoFuego])
    
    pokemon.movimientos=(movimientoAgua, movimientoFuego)
    assert movimientoAgua in pokemon.movimientos