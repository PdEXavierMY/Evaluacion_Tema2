#1) Código a evaluar:
def c1():
    try:
        numero = 7/0
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

#2) Código a evaluar:
def c2(lista):
    try:
        lista[10]
    except IndexError:
        print("La lista no tiene elemento en el índice introducido.")
        
#3) Código a evaluar:
def c3(dicc):
    try:
        dicc["alemania"]
    except KeyError:
        print("No existe una key en el diccionario que se llame así.")

#4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
def c4():
    try:
        resultado = "2" + 10
    except TypeError:
        print("Intentas operar elementos de tipos distintos.")