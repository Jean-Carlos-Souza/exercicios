dic = {}

c = 1
while c < 5:
    nome = str(input('Nome do produto: '))
    custo = int(input('Custo: '))
    dic[nome] = custo
    print(dic)
    c += 1
