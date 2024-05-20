from random import randint
import os

def linha():
    print('-=' * 25)

forca = ['lista', 'anel', 'força', 'cachorro', 'pokemon']
pala = []
suce = []
a = randint(1, len(forca))
palavra = forca[a-1]
for i in palavra:
    pala.append(i)
pala.append(palavra)
tentativas = 0
while tentativas < 5:
    print(f'Sua palavra começa com a letra: {palavra[0]} ')
    ten = str(input('Digite a palavra/caractere: ')).strip().lower()
    linha()
    if ten in pala:
        print(f'Parabens!, a letra/palavra {ten} está na palavra.')
        suce.append(ten)
        if ten == palavra:
            break
        print(f'As caracteres acertadas foram: {suce}')

    else:
        print(f'A letra/palavra {ten} não está dentro.')
        tentativas += 1
        print(f'Número de tentativas restantes: {5 - tentativas}')
        print(f'As caracteres acertadas foram: {suce}')
    linha()
    r = str(input('deseja limpar a tela: s/n ')).strip().lower()
    linha()
    if r == 's':
        os.system('cls')

if tentativas >= 5:
    print('Infelizmente não foi hoje. Tente novamente mais tarde.')
    linha()
else:
    print(f'Parabens! A palavra sorteada foi [{palavra}] e você acertou!')
    linha()
