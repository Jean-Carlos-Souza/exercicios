from time import sleep

n = int(input('Digite um número inteiro positivo: '))

for i in range(1, 11, 1):
    s = n * i
    print(f'{i} x {n} = {s}')
    sleep(0.5)