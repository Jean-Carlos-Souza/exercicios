from random import randint

a = randint(1, 100)
c = 1
while True:
    num = int(input('Digite um número: '))
    if num == a:
        break
    elif num > a:
        print(f'O número [{num}] é maior que o número esperado.')
    elif num < a:
        print(f'O número [{num}] é menor que o número esperado.')
    c += 1
print(f'Parabens por ganhar na sua {c}º tentativa, o número era {a}')