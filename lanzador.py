from ej1 import Ejercicio1 as e1
from ej2 import Ejercicio2 as e2
from ej3 import Ejercicio3 as e3
from ej4 import Ejercicio4 as e4
from ej5 import Ejercicio5 as e5
from introducir import solicitar_introducir_numero_extremo2

def ejecutar():
    eleccion = solicitar_introducir_numero_extremo2("Eliga que ejercicio ejecutar", 1, 5)
    if eleccion == 1:
        juan = e1.Alumno("Juan", 7)
        pepe = e1.Alumno("Pepe", 4)
        sylvia = e1.Alumno("Sylvia", 2.5)
        juan.calificacion()
        pepe.calificacion()
        sylvia.calificacion()
    elif eleccion == 2:
        juan = e2.Alumno("Juan", 7)
        pepe = e2.Alumno("Pepe", 4)
        sylvia = e2.Alumno("Sylvia", 2.5)
        print(juan); print(pepe), print(sylvia)
    elif eleccion == 3:
        a = e3.Producto(1122, "A-steroid", 17, "Spray")
        print(a)
        a.precio = 18
        print(a)
    elif eleccion == 4:
        l = [4, 7, 30, 23, 5]
        d = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
        e4.c1()
        e4.c2(l)
        e4.c3(d)
        e4.c4()
    elif eleccion == 5:
        c = e5.Coche("azul", 4, 150, 1200)
        b = e5.Bicicleta("verde", 2, "X15")
        t = e5.Tren("gris", "muchas", 650, 2)
        lista_objetos = [c, b, t]
        e5.catalogar(lista_objetos); print("\n")
        e5.catalogar(lista_objetos, 0.2); print("\n")
        e5.catalogar(lista_objetos, 4)