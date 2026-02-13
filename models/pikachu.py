from pokemonFuego import PokemonFuego
from pokemonAgua import PokemonAgua
class Pikachu(PokemonFuego):
    def __init__(self, nombre, vida, fuerza, defensa, velocidad):
        super().__init__(nombre, vida, fuerza, defensa, velocidad)