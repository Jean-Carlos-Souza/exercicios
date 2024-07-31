class Carro:
    def __init__(self, marca, modelo, ano, preço):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__preço = preço

    
    def promocao(self, Desconto):
        des = self.__preço * (Desconto / 100)
        self.__preço -= des
        print(f'Novo preço do carro com o desconto de {Desconto} é {self.__preço}')

    def get_info(self):
        print('-' * 66)
        print(f'Marca: {self.__marca}\nModelo: {self.__modelo}\nAno: {self.__ano}\nPreço: {self.__preço}')
        print('-' * 66)

if __name__ == '__main__':

    carro1 = Carro('BMW', 'Scarlet', 2024, 500000)
    carro1.get_info()
    carro1.promocao(10)
    carro1.get_info()