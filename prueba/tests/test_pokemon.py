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
    
def setMovimientosustituyendobien():
    movimientoFuego=Movimiento("llamarada", 95, "fuego")
    movimientoquemar=Movimiento("achicharramiento", 95, "fuego")
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58, movimientos=[movimientoFuego, movimientoFuego, movimientoFuego, movimientoFuego])
    
    pokemon.movimientos=(movimientoquemar, 1)
    assert pokemon.movimientos[0]==movimientoquemar

def setMovimientosustituyendoerror():
    movimientoFuego=Movimiento("llamarada", 95, "fuego")
    movimientoAgua=Movimiento("chorro", 95, "agua")
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58, movimientos=[movimientoFuego, movimientoFuego, movimientoFuego, movimientoFuego])
    
    with pytest.raises(TypeError):
        pokemon.movimientos=(movimientoAgua, movimientoFuego)

def setMovimientolistadoMovimientosBien():
    movimientoFuego=Movimiento("llamarada", 95, "fuego")
    movimientoquemar=Movimiento("achicharramiento", 95, "fuego")
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58)
    pokemon.movimientos=[movimientoFuego, movimientoquemar, movimientoFuego, movimientoquemar]
    assert pokemon.movimientos.count(movimientoFuego)==2 and pokemon.movimientos.count(movimientoquemar)==2

def setMovimientolistadoMovimientosTipoIncompatibleError():
    movimientoFuego=Movimiento("llamarada", 95, "fuego")
    movimientoAgua=Movimiento("chorro", 95, "agua")
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58)
    with pytest.raises(TypeError):
        pokemon.movimientos=[movimientoFuego, movimientoAgua, movimientoFuego, movimientoAgua]

def setMovimientolistadoMovimientosTresError():
    movimientoFuego=Movimiento("llamarada", 95, "fuego")
    movimientoAgua=Movimiento("chorro", 95, "agua")
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58)
    with pytest.raises(IndexError):
        pokemon.movimientos=[movimientoFuego, movimientoAgua, movimientoFuego]
        
def setMovimientolistadoMovimientosCincoError():
    movimientoFuego=Movimiento("llamarada", 95, "fuego")
    movimientoAgua=Movimiento("chorro", 95, "agua")
    pokemon=Pokemon(nombre="pikachu", tipo="fuego", vida=150, fuerza=14, defensa=10, velocidad=58)
    with pytest.raises(IndexError):
        pokemon.movimientos=[movimientoFuego, movimientoAgua, movimientoFuego, movimientoAgua, movimientoAgua]
    