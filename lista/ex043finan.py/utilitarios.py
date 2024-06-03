from categoria import Categoria
from transacao import Transacao

lista_categoria = []
lista_transacao = []


def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)

    lista_categoria.append(nova_categoria)

    return nova_categoria

def cadastrar_transação(descricao, valor, categoria):
    nova_transacao = Transacao(nome= descricao, valor= valor, categoria= categoria)

    lista_transacao.append(nova_transacao)

    return lista_transacao

def saldo_total():
    total = 0

    for t in lista_transacao:
        total += t.valor


    return total