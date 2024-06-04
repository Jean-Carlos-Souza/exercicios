from dataclasses import dataclass

@dataclass
class Retangulo:
    largura: float
    altura: float


    def calcular_area(self):
        return self.altura * self.largura
    

    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)
    

altura = float(input('altura: '))
largura = float(input('Largura: '))
    
retangulo1 = Retangulo(altura, largura)
area = retangulo1.calcular_area()
peri = retangulo1.calcular_perimetro()
print(retangulo1 ,area, peri)