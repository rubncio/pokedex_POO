class Movimiento:
    def __init__(self, nombre, porcentajeDaño, tipo):
        self.nombre=nombre
        self.porcentajeDaño=porcentajeDaño
        self.tipo=tipo

    @staticmethod
    def fromDict(diccionario:dict):
        movimiento=Movimiento(
            diccionario.get("nombre"),
            diccionario.get("porcentaje")
            diccionario.get("tipo"),
        )
        return pokemon