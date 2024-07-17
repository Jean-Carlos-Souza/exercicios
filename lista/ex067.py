lista_dic = [
    {'nome':'Bola', 'preço':10, 'quantidade':3},
    {'nome':'piscina', 'preço':100, 'quantidade':1},
    {'nome':'teclado', 'preço':20, 'quantidade':5},
    {'nome':'tela', 'preço':50, 'quantidade':15}
]

lista_dic.append({'nome':'celular', 'preço':500, 'quantidade':2})
lista_dic.append({'nome':'livro', 'preço':10, 'quantidade':8})

lista_dic[1]['quantidade'] = 2

for i in lista_dic:
    print(i)

print('-----------------------')

for i in lista_dic:
    valor_total = i['preço'] * i['quantidade']  
    print(f'O produto: {i['nome']}, tem o valor em estoque: {valor_total:.2f}')
