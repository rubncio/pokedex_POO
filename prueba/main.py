import random
from pokemon import Pokemon
from movimiento import Movimiento
# Script que me va a ejecutar la logica siguiente:

# Escenario
# Definir que pokemons van a combatir (2 -> p1 y p2)
# Definir quien inicia el ataque: el que tenga más velocidad
# Logica de turno: 
# - 1 accion por turno para cada pokemon
# - ataca 1 pokemon el 2 recibe daño en función del p1.ataque - p2.defensa
# - ataca 2 pokemon el 1 recibe daño en función del p2.ataque - p1.defensa

# condiciones victoria o derrota
# El primer pokemon que se queda a vvida <= 0 pierde

#luego añadir clase movimiento nombre, dañoporcentaje, 
if __name__=="__main__":
    """self.nombre=nombre
        self.tipo=tipo
        self.nivel=nivel
        self.vida=vida
        self.fuerza=fuerza
        self.defensa=defensa
        self.velocidad=velocidad
        self.movimientos=movimientos
        
        Vida (Inicial 100-300)
# - Fuerza (Maz 20)
# - Defensa (Max 18)
# - Velocidad (Max 100)
# - movimientos[4] - Solo nombre"""
    pokemon1=Pokemon(nombre="pikachu", tipo="fuego", nivel=4, vida=150, fuerza=5, defensa=10, velocidad=58, movimientos=[Movimiento("fuego",33),Movimiento("agua",95),Movimiento("naturaleza",41),Movimiento("magia",50)]
    )
    pokemon2=Pokemon(nombre="obama", tipo="politico", nivel=6, vida=250, fuerza=15, defensa=13, velocidad=35, movimientos=[Movimiento("economia",100),Movimiento("Igualdad",67),Movimiento("Demagogia",85),Movimiento("Dialogo",47)]
    )

    primerAtacante=""
    segundoAtacante=""
    if(pokemon1.velocidad>pokemon2.velocidad):
        primerAtacante=pokemon1
        segundoAtacante=pokemon2
    elif(pokemon2.velocidad>pokemon1.velocidad):
        primerAtacante=pokemon2
        segundoAtacante=pokemon1
    else:
        primerAtacante=random.choice([pokemon1, pokemon2])
        if  primerAtacante==pokemon2:segundoAtacante=pokemon1 
        else:segundoAtacante=pokemon2
        #se decide aleatoriamente
    pokemonGanador:Pokemon
    turno=1
    while(True):
        
        print(f"Turno :{turno}")
        primerAtacante.ejecutar_movimiento(segundoAtacante)
        if(segundoAtacante.derrotado):
            pokemonGanador=primerAtacante
            break
        segundoAtacante.ejecutar_movimiento(primerAtacante)
        if(primerAtacante.derrotado):
            pokemonGanador=segundoAtacante
            break
        turno+=1
    print(f"el ganador es {pokemonGanador.nombre}")