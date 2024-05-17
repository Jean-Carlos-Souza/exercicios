def soma(l):
    s = 0
    for i in l:
        s += i
    return s


lista = []
while True:
    n = int(input('Digite um número: '))
    if n in lista:
        print('Erro, número já esta dentro da lista!')
    else:
        lista.append(n)
    r = str(input('Quer continuar: ')).strip().upper()
    if r == 'N':
        break
lista.sort()
for i in lista:
    print(i,'...', end='')
print()
resp = soma(lista)
print(f'A soma de todos os números listado é: {resp}')
