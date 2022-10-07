class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, modelo):
        self.color = color
        self.ruedas = ruedas
        self.modelo = modelo


class Tren(Vehiculo):
    def __init__(self, color, ruedas, longuitud, antiguedad):
        self.color = color
        self.ruedas = ruedas
        self.longuitud = longuitud
        self.antiguedad = antiguedad

def catalogar(lista, rueda=0):
    cont = 0
    nruedas = 0
    for elemento in lista:
        if rueda != 0:
            if elemento.ruedas == rueda:
                nruedas += 1
                print("Se han encontrado {} vehículos con {} ruedas: {}".format(nruedas, rueda, type(elemento).__name__))
        cont += 1
        print("El nombre del vehiculo {} es {}".format(cont, type(elemento).__name__))