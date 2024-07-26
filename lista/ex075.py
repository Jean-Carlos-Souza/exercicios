def separador():
    print('-' * 66)

class Produto:
    def __init__(self, nome, preço, quantidade):
        self.__nome = nome
        self.__preço = preço
        self.__quantidade = quantidade

    def atualizar_quanti(self, Nova_Quanti):
        separador()
        print(f'A quantidade de {self.__nome} passou de {self.__quantidade} -> ', end='')
        self.__quantidade = Nova_Quanti
        print(f'{self.__quantidade}')
        separador()

    def Get_Exibir_info(self):
        separador()
        print(f'Produto: {self.__nome}\nPreço: {self.__preço}\nQuantidade Disponível: {self.__quantidade}')
        separador()

if __name__ == '__main__':

    produto1 = Produto('sorvete', 15, 10)
    produto1.Get_Exibir_info()
    produto1.atualizar_quanti(20)
    produto1.Get_Exibir_info()

    dados = [
        {'nome':'bola', 'preço':10, 'quantidade':4},
        {'nome':'teclado', 'preço':50, 'quantidade':10}
    ]

    produtos = [Produto(i['nome'], i['preço'], i['quantidade']) for i in dados]

    produtos[1].atualizar_quanti(30)

    for i in produtos:
        i.Get_Exibir_info()