from time import sleep

def menu():
    while True:
        print('-' * 60)
        a = 'ESCOLHA UMA DAS OPÇÕES'
        print(f'{a:^60}')
        print('[1] - Lista de Livros\n[2] - Adicionar um livro\n[3] - Remover um livro\n[4] - Exibir informações de um livro\n[5] - Sair do Sistema')
        esc = int(input('Qual opção escolhida: '))
        if esc == 1:
            s = lista_de_livros()
            if s == 5:
                saindo()
                break
        elif esc == 2:
            s = adicionar_um_livro()
            if s == 5:
                saindo()
                break
        elif esc == 3:
            s = remover_um_livro()
            if s == 5:
                saindo()
                break
        elif esc == 4:
            return esc
        elif esc == 5:
            saindo()
            break
        else:
            print('Opções não registrada, tente novamente!')
        print('-' * 60)

def saindo():
    print('Saindo do sistema...')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Obrigado por utilizar!')

def lista_de_livros():
    sleep(0.5)
    while True:
        print('-' * 60)
        for i in lista:
            print(f'{i}')
            print('')
        print('-' * 60)
        print('[1] - Voltar para o menu\n[2] - Sair do sistema')
        esc = int(input('Qual opção escolhida: '))
        if esc == 1:
            break
        elif esc == 2:
            return 5
        else:
            print('-' * 60)
            print('Opção inválida! Tente novamente')

def adicionar_um_livro():
    sleep(0.5)
    while True:
        print('-' * 60)
        a = str(input('Nome do livro: '))
        if a in lista:
            print('')
            print('Livro já existe na lista!')
        else:
            lista.append(a)
        print('-' * 60)
        print('[1] - Adicionar outro livro\n[2] - Voltar para o menu\n[3] - Sair do sistema')
        esc = int(input('Qual opção escolhida: '))
        if esc == 1:
            pass
        elif esc == 2:
            break
        elif esc == 3:
            return 5
        else:
            print('Opção inválida! Tente novamente')
        
def remover_um_livro():
    sleep(0.5)
    while True:
        print('-' * 60)
        for i, v in enumerate(lista):
            print(f'[{i}] - {v}')
            print('')
        esc = int(input('Qual número do livro deseja remover: '))
        if esc > len(lista):
            print('')
            print(f'Número inválido! digite outro.')
            print('')
        else:
            for i, v in enumerate(lista):
                if esc == i:
                    re = v
            lista.remove(re)
            print('')
            print('Livro removido com Sucesso!')
            print('')
            print('[1] - Remover outro livro\n[2] - Voltar para o menu\n[3] - Sair do sistema')
            esc = int(input('Qual opção escolhida: '))
            if esc == 1:
                pass
            elif esc == 2:
                break
            elif esc == 3:
                return 5
            else:
                print('Opção inválida! Tente novamente')


class Livro:
    def __init__(self, titulo, autor, ano, preço):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__preço = preço

    def get_info(self):
        print('-' * 60)
        a = 'INFORMAÇÕES DO LIVRO'
        print(f'{a:^60}')
        print('')
        print(f'NOME: {self.__titulo}\nAUTOR: {self.__autor}\nANO: {self.__ano}\nPREÇO: {self.__preço}')
        print('-' * 60)


lista = ['hp 1', 'hp 2', 'hp 3']

menu()
