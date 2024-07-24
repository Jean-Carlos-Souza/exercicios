produtos = [
    {'nome': 'agua', 'preço': 2, 'quantidade': 10},
    {'nome': 'coca', 'preço': 5, 'quantidade': 5},
    {'nome': 'pepsi', 'preço': 4, 'quantidade': 6},
    {'nome': 'h2o', 'preço': 7, 'quantidade': 2}
]

print(produtos)

print('-' * 55)

for i in produtos:
    print(i, '\n')

print('-' * 55)

produtos.append({'nome': 'salgado', 'preço': 6, 'quantidade': 8})
produtos.append({'nome': 'bola', 'preço': 4, 'quantidade': 1})

print('-' * 55)

for i in produtos:
    print(i, '\n')


print('-' * 55)

for i in produtos:
    print(f'O item [{i['nome']}] tem disponíveis [{i['quantidade']}] no estoque')

print('-' * 55)

c = 0
mais_caro = produtos[0]
while c < len(produtos):
    if produtos[c]['preço'] > mais_caro['preço' ]:
        mais_caro = produtos[c] 
    c += 1
print(f'O produto mais caro da lista é [{mais_caro['nome']}] custando o total de [{mais_caro['preço']}]')

print('-' * 55)
