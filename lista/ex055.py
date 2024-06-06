n = int(input('Numero inteiro: '))
c = 1
s = 0
while True:
    c += 1
    if c > n:
        break
    print(f'{c}... ', end='')
    s += n
print(f'A soma de todos esses números é {s}')

