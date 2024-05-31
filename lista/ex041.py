
# primeiro contato com POO :)
class Carro():

    def __init__(self, marca, velocidade_max, tempo_de_parada):
        self.marca = marca
        self.velocidade_max = velocidade_max
        self.tempo_de_parada = tempo_de_parada
        pass

carro1 = Carro('ferrari', '120', '6')
carro2 = Carro('mercedes', '100', '12')
carro3 = Carro('sport', '300', '0.5')
carro4 = Carro(str(input('carro: ')), str(input('velocidade: ')), str(input('tempo de parada: ')))
print(carro1.marca, carro1.tempo_de_parada, carro1.velocidade_max)
print(carro2.marca, carro2.tempo_de_parada, carro2.velocidade_max)
print(carro3.marca, carro3.tempo_de_parada, carro3.velocidade_max)
print(carro4.marca, carro4.tempo_de_parada, carro4.velocidade_max)