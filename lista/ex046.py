import math
from dataclasses import dataclass


@dataclass
class Circulo:
    raio: float

    def calcular_area(self):
        return math.pi * self.raio
    
    def calcular_circuferencia(self):
        return 2 * math.pi * self.raio
    
circulo1 = Circulo(20)
circulo1_area = circulo1.calcular_area()
circulo1_circufe = circulo1.calcular_circuferencia()
print(circulo1, circulo1_circufe, circulo1_area)
circulo2 = Circulo(15)
circulo2_area = circulo2.calcular_area()
circulo2_circufe = circulo2.calcular_circuferencia()
print(circulo2, circulo2_circufe, circulo2_area)