from prueba.pokemon import Pokemon

class PokemonAgua(Pokemon):
    def __init__(self, nombre, vida, fuerza, defensa, velocidad):
        super().__init__(nombre, vida, fuerza, defensa, velocidad)
        self.tipo.append("Agua")