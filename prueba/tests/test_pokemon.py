import pytest
from pokemon import Pokemon
from movimiento import Movimiento
from exceptions.oponenteVacio import OponenteVacio

pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58)

def ejecutarMovimientoOponenteVacio():
    with pytest.raises(OponenteVacio):
        pokemon.ejecutar_movimiento()

def setMovimientoIncompatible():
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58)
    movimientoAgua=Movimiento("chorro", 95, "agua")
    with pytest.raises(TypeError):
        
        pokemon.setMovimiento(movimientoAgua)

def setMovimientoCompatible():
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58)
    movimientoFuego=Movimiento("achicharramiento", "fuego", 95)
    pokemon.setMovimiento(movimientoFuego)
    assert len(pokemon.getMovimientos()) == 1

def setMovimientoMasDeCuatro():
    pokemon=Pokemon(nombre="pikachu", tipo="agua", vida=150, fuerza=14, defensa=10, velocidad=58)
    movimientoAgua=Movimiento("chorro", 95, "agua")
    pokemon.setMovimiento(movimientoAgua)
    pokemon.setMovimiento(movimientoAgua)
    pokemon.setMovimiento(movimientoAgua)
    pokemon.setMovimiento(movimientoAgua)
    with pytest.raises(IndexError):
        pokemon.setMovimiento(movimientoAgua)
    
