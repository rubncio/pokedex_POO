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
    def __init__(self, nombre, tipo, vida, fuerza, defensa, velocidad):
        self.nombre=nombre
        self.tipo=tipo
        self.vida=vida
        self.fuerza=fuerza
        self.defensa=defensa
        self.velocidad=velocidad
        self.derrotado=False
    
    """def setMovimiento(self, movimiento:Movimiento):
        if len(self.__movimientos)>=4:
            raise IndexError("Solo se permiten hasta 4 movimientos")
        if self.tipo!=movimiento.tipo:
            raise TypeError("tipo de movimiento no permitido para este pokemon")
        self.__movimientos.append(movimiento)"""
    @property
    def movimientos(self):
        return self.__movimientos.copy()

    @__movimientos.setter
    def movimientos(self, movimiento):
        if type(movimiento)==movimiento:
            #En caso de que se indique como valor para el setter un objeto de movimiento
            if len(self.__movimientos)<4:
                if self.tipo == movimiento.tipo:
                    self.__movimientos.append(movimiento)
                else:
                    raise TypeError("tipo/s de movimiento no permitido para este pokemon")
                
            else:
                raise IndexError("Este pokemon ya tiene 4 movimientos")

        elif type(movimiento)==list:
            #En caso de que se indique como valor para el setter un list de objetos de movimiento
            #Si se indica una lista tiene que ser 4 movimientos 
            if len(movimiento)!=4:
                assert IndexError("Solo se permiten 4 movimientos")
            else:
                if all(self.tipo == mov.tipo for mov in movimiento):
                    self.__movimientos=movimiento
                else:
                    raise TypeError("tipo/s de movimiento no permitido para este pokemon")
        elif type(movimiento)==tuple:
            #En caso de que se indique como valor para el setter una tupla en elq ue se indique el movimiento y el indice a sustituir.
            nuevoM=movimiento[0]
            indice=movimiento[1]
            if indice <1 or indice >4:
                raise TypeError("indice a reemplazar tiene que ser entre 1 a 4")
            if self.tipo == nuevoM.tipo:
                self.__movimientos.pop(indice)
                self.__movimientos.append(nuevoM)
            else:
                raise TypeError("tipo/s de movimiento no permitido para este pokemon")
            
        

    def getMovimientos(self)->Movimiento:
        return self.__movimientos

    def ejecutar_movimiento(self, pokemonOponente):
        if pokemonOponente==None :raise(OponenteVacio)
        movimiento: Movimiento=random.choice(self.movimientos)
        ataque=self.fuerza*(1+(movimiento.porcentajeDaño/100))
        print(f"{self.nombre}:Lanzo el ataque:{movimiento.nombre} con un daño de {ataque:.0f}")
        dañoAtaque=ataque-pokemonOponente.defensa

        pokemonOponente.recibirdano(dañoAtaque)

    def recibirdano(self, dañoAtaque):
        self.vida-=dañoAtaque
        if(self.vida<=0):
            print(f"{self.nombre}: He caido")
            self.derrotado=True
        else:
            print(f"{self.nombre}: Me defiendo y lo resisto")