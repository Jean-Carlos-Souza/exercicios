from dataclasses import dataclass

@dataclass
class Carro:
    modelo:str
    marca:str
    ano:int

    def interface(self):
        print(f'Carro: \033[31m{self.modelo}\033[m | Marca: \033[32m{self.marca}\033[m | Ano: \033[33m{self.ano}\033[m')

carro1 = Carro('ferrari sport', 'ferrari', 2020)
carro1.interface()