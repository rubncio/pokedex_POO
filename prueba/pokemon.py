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
from exceptions.oponenteVacio import OponenteVacio
from movimiento import Movimiento


class Pokemon:
    __movimientos:list=list()
    def __init__(self, nombre, tipo, vida, fuerza, defensa, velocidad, movimientos):
        self.nombre=nombre
        self.tipo=tipo
        self.vida=vida
        self.fuerza=fuerza
        self.defensa=defensa
        self.velocidad=velocidad
        self.derrotado=False
        self.__movimientos=movimientos
    
    def setMovimiento(self, movimiento:Movimiento):
        if len(self.__movimientos)>=4:
            raise IndexError("Solo se permiten hasta 4 movimientos")
        if self.tipo!=movimiento.tipo:
            raise TypeError("tipo de movimiento no permitido para este pokemon")
        self.__movimientos.append(movimiento)

    @__movimientos.setter
    def movimientos(self, movimiento):
        if type(movimiento)==movimiento:
            if len(self.__movimientos)<4:
                self.__movimientos.append(movimiento)
            else:
                raise IndexError("Este pokemon ya tiene 4 movimientos")

        elif type(movimiento)==list:
            if len(movimiento)!=4:
                assert IndexError("Solo se permiten 4 movimientos")
            else:
                if all(self.tipo == mov.tipo for mov in movimiento):
                    self.__movimientos=movimiento
                else:
                    raise TypeError("tipo/s de movimiento no permitido para este pokemon")
        elif type(movimiento)==tuple:
            nuevoM=movimiento[0]
            reempM=movimiento[1]
            self.__movimientos.remove(reempM)
            self.__movimientos.append(nuevoM)
        

    def getMovimientos(self)->Movimiento:
        return self.__movimientos

    def ejecutar_movimiento(self, pokemonOponente):
        if pokemonOponente==None :raise(OponenteVacio)
        movimiento: Movimiento=random.choice(self.movimientos)
        ataque=self.fuerza*(1+(movimiento.porcentajeDaño/100))
        print(f"{self.nombre}:Lanzo el ataque:{movimiento.nombre} con un daño de {ataque:.0f}")
        dañoAtaque=ataque-pokemonOponente.defensa

        pokemonOponente.recibirdaño(dañoAtaque)

    def recibirdano(self, dañoAtaque):
        self.vida-=dañoAtaque
        if(self.vida<=0):
            print(f"{self.nombre}: He caido")
            self.derrotado=True
        else:
            print(f"{self.nombre}: Me defiendo y lo resisto")