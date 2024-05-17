def multipli(a):
    t = 1
    for i in a:
        t *= i
    return t
    

multi = []
while True:
    a = int(input('Nu: '))
    if a not in multi:
        multi.append(a)
    r = str(input('Quer continuar: ')).strip().upper()
    if r == 'N':
        break
re = multipli(multi)
multi.sort()
print(f'A multiplicação da lista: ',end='')
for i in multi:
    print(f'[{i}]', end=' ')
print(f': {re}')