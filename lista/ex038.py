import os
from time import sleep

l1 = ['casinha', 'casebre', 'casarão', 'casar']
l2 = ['felicidade', 'felizardo', 'felicitar', 'felicita-lo']
l3 = ['solar', 'solário', 'solene', 'insolente']
l4 = ['rapizes', 'rapidamente', 'rapidíssimo', 'velocidade']
l5 = [1,2,3,4]
dic = {
    '[1] - casa':l1,
    '[2] - feliz':l2,
    '[3] - sol': l3,
    '[4] - rapido': l4
}
print('-' * 40)
print('|  ESCOLHA UMA DAS SEGUINTES PALAVRAS  |')
print('-' * 40)
for i in dic.keys():
    print(i)
print('-' * 40)
while True:
    a = int(input('Qual deseja escolher: '))
    if a in l5:
        print('-' * 40)
        break
if a == 1:
    print(f'As derivações da palavra são as seguintes: ', end='')
    for i in dic['[1] - casa']:
        print(f'[{i}] -- ', end='')
    print()
elif a == 2:
    print(f'As derivações da palavra são as seguintes: ', end= '')
    for i in dic['[2] - feliz']:
        print(f'[{i}] -- ', end='')
    print()
elif a == 3:
    print(f'As derivações da palavra são as seguintes: ', end='')
    for i in dic['[3] - sol']:
        print(f'[{i}] -- ', end='')
    print()
else:
    print(f'As derivações da palavra são as seguintes: ', end='')
    for i in dic['[4] - rapido']:
        print(f'[{i}] -- ', end='')
    print()

sleep(5)
os.system('cls')


