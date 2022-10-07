class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return "El alumno se ha creado con éxito"

    def calificacion(self):
        if self.nota >= 5:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")

juan = Alumno("Juan", 7)
pepe = Alumno("Pepe", 4)
sylvia = Alumno("Sylvia", 2.5)
juan.calificacion()
pepe.calificacion()
sylvia.calificacion()