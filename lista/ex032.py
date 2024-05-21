a = []
a1 = []
while True:
    b = int(input('Digite um número: '))
    if b not in a:
        a.append(b)
    r = str(input('Deseja continuar: s/n ')).strip().upper()
    if r == 'N':
        break
for i in a[::-1]:
    a1.append(i)
print('Sua lista normal é: ', end='')
for i in a:
    print(i,'...', end='')
print()
print('Sua lista reversa é: ',end='')
for i in a1:
    print(i,'...', end='')