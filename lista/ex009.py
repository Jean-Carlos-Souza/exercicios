def ve(b):
    if b % 2 == 0:
        return 'Par'
    else:
        return 'Impar'


a = int(input('Numero: '))
res = ve(a)
print(f'O número {a} é {res}')
