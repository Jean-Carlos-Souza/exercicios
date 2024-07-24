def linha():
    print('-=' * 40)

class Funcionario: 
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__sal = salario

    def aumento_salario(self, automento_em_porcentagem):
        aumento = self.__sal * (automento_em_porcentagem / 100)
        print(f'Seu salário aumento em {automento_em_porcentagem} %, indo de  R${self.__sal} para ', end='')
        self.__sal = self.__sal + aumento
        print(f'R${self.__sal}')

    def diminuir_salario(self, diminuição_em_porcentagem):
        dimi = self.__sal * (diminuição_em_porcentagem / 100)
        print(f'Seu salário diminuiu em {diminuição_em_porcentagem} %, indo de  R${self.__sal} para ', end='')
        self.__sal -= dimi
        print(f'R${self.__sal}')

    def get_info_do_funci(self):
        linha()
        print(f'FUNCIONÁRIO: {self.__nome:>10}\nCARGO: {self.__cargo:>16}\nSALÁRIO:     {self.__sal:>10}')
        linha()
    

funci1 = Funcionario('Jean', 'Desenvolvedor', 2000)
funci1.get_info_do_funci()
funci1.aumento_salario(20)
funci1.get_info_do_funci()
funci1.diminuir_salario(50)
funci1.get_info_do_funci() 


