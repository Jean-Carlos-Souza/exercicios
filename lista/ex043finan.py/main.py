from categoria import Categoria
from transacao import Transacao


c = Categoria(nome = 'Receita')

t = Transacao(
            nome= 'salário de 2020/01',
            valor=2500,
            categoria=c
)
t2 = Transacao(
            nome= 'salário de 2020/01',
            valor=2500,
            categoria=c
)
t3 = Transacao(
            nome= 'salário de 2020/01',
            valor=2500,
            categoria=c
)
t4 = Transacao(
            nome= 'salário de 2020/01',
            valor=2500,
            categoria=c
)


t4.exibir()