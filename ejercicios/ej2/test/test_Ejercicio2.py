import copy
import os
import sys
import inspect
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import Ejercicio2 as e2

class TestEj1(unittest.TestCase):
    def setUp(self):
        lista = [e2.Alumno("Juan", 2), e2.Alumno("Pepe", 3), e2.Alumno("Sylvia", 9)]

    def test_calificacion(self):
        bcatalogado = e2.Alumno("Juan", 2).calificacion()