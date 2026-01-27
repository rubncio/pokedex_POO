# Clase pokemon

## Atributos
# - Nombre
# - Tipo
# - Nivel
# - Vida (Inicial 100-300)
# - Fuerza (Maz 20)
# - Defensa (Max 18)
# - Velocidad (Max 100)
# - movimientos[4] - Solo nombre

## Metodos
# ejecutar_movimiento(self, otro_pokemon) 
# Se decide aleatoriamente entre los 4 movimientos disponibles en el pokemon
# Lanza este movimiento
# se calcula el daño y se ejecuta la funciñon recibir dano del otro pokemon
# daño = self.ataque - otro_pokemon.defensa


# recibir_dano()
# Se resta a la vida actual el daño recibido
import random


class Pokemon:
    def __init__(self, nombre, tipo, nivel, vida, fuerza, defensa, velocidad, movimientos):
        self.nombre=nombre
        self.tipo=tipo
        self.nivel=nivel
        self.vida=vida
        self.fuerza=fuerza
        self.defensa=defensa
        self.velocidad=velocidad
        self.movimientos=movimientos
    
    def ejecutar_movimiento(self, pokemonOponente):
        ataqueint=random.randint(1,4)
        ataque=self.movimientos[ataqueint]
        print(f"{self.nombre} ha lanzado el ataque:{ataque}")
        dañoAtaque=self.fuerza-pokemonOponente.defensa

        pokemonOponente.recibirdaño(dañoAtaque)

    def recibirdaño(self, dañoAtaque):
        self.vida-=dañoAtaque
        