

class Veiculo:

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo             # o __ antes do atributo, deixa eles privados
        self.__num_registro = None         # impossibilitando o acesso direto

    def movimentar(self):
        print('Estou me movimentando')

    #Para gravar um dado em um elemento, Setter
    def set_numeroDoRegistro(self, registro):
        self.__num_registro = registro



    #para acessar um alemento com __, se uso o metodo Getter
    #serve para da privacidade e segurança para os dados
    def get_fa_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')

    def get_num_registro(self):
        return self.__num_registro


class Carro(Veiculo):
    # Método init será herdado

    def correr(self):
        print('Sou um carro e estou correndo')


class Avião(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        #metodo super() faz com que ele herder as caracteristicas de outra __init__ nessa nova __init__
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print('Eu voo alto')

if __name__ == '__main__':
    meu_veiculo = Veiculo('Gm', 'Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fa_modelo()
    #print(meu_veiculo.fabricante, meu_veiculo.modelo)
    meu_veiculo.set_numeroDoRegistro(12345)
    print(f'Registro: {meu_veiculo.get_num_registro()}\n')

    print('-' * 55)

    meu_carro = Carro('ferrari', '23Gen')
    meu_carro.correr()
    meu_carro.get_fa_modelo()

    print('-' * 55)

    meu_avião = Avião('Boll', 'Brasil', 'Bong')
    meu_avião.movimentar()
    meu_avião.get_fa_modelo()
    print(f'Categoria: {meu_avião.get_categoria()}')