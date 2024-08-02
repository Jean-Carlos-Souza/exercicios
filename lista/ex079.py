def linha():
    print('-' * 60)


class Produto:
    def __init__(self,nome, preço, quantidade, categoria):
        self.__nome = nome
        self.__preço = preço
        self.__quantidade = quantidade
        self.__categoria = categoria

    def Atualizar_quantidade(self, Nova_quantidade):
        linha()
        print(f'{self.__nome}: {self.__quantidade} --> ',end='')
        self.__quantidade = Nova_quantidade
        print(f'{self.__quantidade}')   

    def Exibir_info(self):
        linha()
        print(f'Produto: {self.__nome}\nPreço: {self.__preço}\nQuantidade: {self.__quantidade}\nCategoria: {self.__categoria}')

    def get_produto(self):
        print(self.__nome)


produtos = []

def adicionar_produtos():
    linha()
    nome = str(input('Digite o nome do produto: ')).strip()
    preço = int(input('Preço do produto: '))
    quantidade = int(input(f'Quantidade de {nome}: '))
    categoria = str(input(f'Categoria do {nome}: ')).strip()
    produto = Produto(nome, preço, quantidade, categoria)
    produtos.append(produto)
    print('Produto adicionado com sucesso!')


def remover_produto():
    linha()
    for p in produtos:
        get_produto()
    nome = str(input('Digite o nome do produto que deseja remover: ')).strip()
    for i in produtos:
        if i.nome == nome:
            produtos.remove(i)
            print('Produto removido com sucesso!')
        else:
            print('Produto não encontrado!')

def exibir_todos_os_produtos():
    linha()
    if not produtos:
        print('Nenhum produto cadastrado')
    else:
        for pro in produtos:
            pro.Exibir_info()

def menu():
    linha()
    print('''
            Menu de Opções
            1 - Adicionar novo Produto
            2 - Remover Produto
            3 - Atualizar quantidade do Produto
            4 - Exibir todos os Produtos
            5 - Sair
''')
    a = int(input('Escolha uma das opções: '))
    return a
while True:
    linha()
    op = menu()
    if op == 1:
        adicionar_produtos()
    elif op == 2:
        remover_produto()
    elif op == 3:
        nome = str(input('Digite o nome do produto que deseja alter a quantidade: ')).strip()
        for produto in produtos:
            if produto.nome == nome:
                novaQuantidade = int(input('Digite a nova quantidade: '))
                produto.Atualizar_quantidade(novaQuantidade)
                print('Quantidade de produtos atualizados')
                break
        else:
            print('Produto não encontrado')
    elif op == 4:
        exibir_todos_os_produtos()
    elif op == 5:
        print('Saindo....')
        break
    else:
        print('Opção não encontrada! Tente novamente.')           
    
