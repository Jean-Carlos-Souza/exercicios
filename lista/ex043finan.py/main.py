from utilitarios import (
    cadastrar_categoria,
    cadastrar_transação,
    saldo_total
)


cadastrar_receitas = cadastrar_categoria('receitas')
cadastrar_contas = cadastrar_categoria('contas fixas')
cadastrar_lazer = cadastrar_categoria('lazer')
cadastrar_viagem = cadastrar_categoria('viagem')

cadastrar_transação(
    descricao= 'salário jan/2024',
    valor= 1000.0,
    categoria= cadastrar_receitas
)

cadastrar_transação(
    descricao= 'mesada',
    valor= 50,
    categoria= cadastrar_receitas
)

cadastrar_transação(
    descricao= 'show',
    valor= -150,
    categoria= cadastrar_lazer
)

cadastrar_transação(
    descricao= 'contas de luz',
    valor= -250,
    categoria= cadastrar_contas
)

cadastrar_transação(
    descricao= 'viagem disney',
    valor= -400,
    categoria= cadastrar_viagem
)

total = saldo_total()

print('Saldo total: ', total)