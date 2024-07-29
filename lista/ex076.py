def linha():
    print('-' * 30)

def interface():
    linha()
    print(f'{'BEM VINDO':^30}')
    linha()
    resp = input('Registrar um aluno [1]: \n').strip()
    return resp


class Aluno:
    def __init__(self, nome, idade, n1, n2, n3, n4):
        self.__nome = nome
        self.__idade = idade
        notas = [n1, n2, n3, n4]
        self.__notas = notas
    
    def get_Média(self):
        print('-' * 66)
        a = 0
        for i in self.__notas:
            a += i
        self.__media = a / 4
        print(f'A média do aluno {self.__nome} é [{self.__media:.2f}]')
    
    def get_info(self):
        print('-' * 66)
        print(f'Nome: {self.__nome}\nIdade: {self.__idade}\nNotas: ',end='')
        for i in self.__notas:
            print(f'{i}, ', end='')
        print(f'\nMédia: {self.__media}')
        print('-' * 66)

aluno1 = Aluno('Jean', 21, 10, 8, 2, 10)
aluno1.get_Média()
aluno1.get_info()
resp = interface()

