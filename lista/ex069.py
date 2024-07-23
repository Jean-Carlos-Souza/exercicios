lista = [
    {'nome':'jean', 'idade':21, 'nota':10},
    {'nome': 'Ana', 'idade':19, 'nota':6}
]

lista.append({'nome': 'ma', 'idade':28, 'nota':8})

print('--------------------------')

for i in lista:
    print('=' * 50)
    print(i)

print('--------------------------')

nome = str(input(f'Qual nome deseja alterar: \n{lista[0]['nome']} \n{lista[1]['nome']}\n{lista[2]['nome']}\n')).lower().strip()

notas = int(input('Qual é a nova nota: '))

for i, v in enumerate(lista):
    for valor in v.values():
        if valor == nome:
            lista[i]['nota'] = notas

for i in lista:
    print('-' * 50)
    print(i)
        

print('-' * 50)

c = 0
media = 0
for i in lista:
    c += 1
    media = media + i['nota']

media_geral = media / c
print(f'{media_geral:.2f}')
        


