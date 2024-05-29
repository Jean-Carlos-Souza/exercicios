import os
from time import sleep
def somar(a, b):
    s = a + b
    return s

def dim(a, b):
    s = a - b
    return s

def divi(a, b):
    s = a / b
    return s

def resto(a, b):
    s = a % b
    return s


a1 = float(input('N1: '))
a2 = float(input('N2: '))
while True:
    a3 = str(input('Qual sinal deseja: |+|-|/|%| '))
    if a3 in '+-/%':
        break
if a3 == '+':
    r = somar(a1, a2)
    print(f'A soma dos números [{a1}] e [{a2}] = [{r}]')
elif a3 == '-':
    r = dim(a1, a2)
    print(f'O número [{a1}] - [{a2}] = [{r}]')
elif a3 == '/':
    r = divi(a1, a2)
    print(f'A divisão dos números [{a1}] e [{a2}] = [{r}]')
else:
    r = resto(a1, a2)
    print(f'O resto da divisão dos números [{a1}] e [{a2}] = [{r}]')
print('Terminou')
print('Desligando em...')
for c in range(5, 0, -1):
    print(f'{c}..', end='')
    print()
sleep(3)
os.system('cls')
