


def quadrado(li):
    for i in li:
        a = pow(i[0], 2)
        q.clear()
        q.append(a)
        quadra.append(q[:])

q = []
quadra = []
lis = []
va = []
while True:
    va.clear()
    va.append(int(input('Numero: ')))
    lis.append(va[:])
    res = str(input('Continuar: s/n ')).strip().upper()
    if res == 'N':
        break
quadrado(lis)
print(f'A lista original é: ')
for i in lis:
    print(i, end='')
print()
print(f'A lista ao quadrado é: ')
for i in quadra:
    print(i, end='')