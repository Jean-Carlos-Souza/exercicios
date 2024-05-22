import os

lis = []
a = str(input('String: ')).strip().split()
for i in a:
    if i not in lis:
        lis.append(i)
os.system('cls')
print('-=' * 20)
print('String sem modificação: ')
print('-=' * 20)
for i in a:
    print(f'[{i}]',end='')
print()
print('-=' * 20)
print('String Com a modificação de palavras unicas: ')
print('-=' * 20)
for i in lis:
    print(f'[{i}]', end='')
print()
print(f'O número de palavras únicas na string apresentada é [{len(lis)}]')