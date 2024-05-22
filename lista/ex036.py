def fac(b=0):
    for i in range(b +1):
        if i != 0:
            lis.append(i)
    lis.sort(reverse=True)
    s = 1
    for i in lis:
        s *= i
    return s

lis = []
a = int(input('Número inteiro: '))
r = fac(a)
print(f'O fatorial de {a} é {r}')