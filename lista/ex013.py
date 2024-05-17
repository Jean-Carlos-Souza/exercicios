def quadra(a1):
    for i in a1:
        x = pow(i,2)
        nu2.append(x)

nu2 = []
nu1 = []
while True:
    n = int(input('Número: '))
    if n in nu1:
        print('Digite outro número.')
    else:
        nu1.append(n)
    r = str(input('Quer continuar: s/n ')).strip().upper()
    if r == 'N':
        break
quadra(nu1)
print(nu2)
