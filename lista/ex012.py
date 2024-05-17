from time import sleep


def visua(l, b):
    if b in l:
        return True
    else:
        return False


li = [1,3,5,6]
a = int(input('Escreva um número até 10: '))
resp = visua(li, a)
print(f'O número [{a}] está dentro da lista?????')
sleep(1.5)
print(resp)
if resp == True:
    print(f'Parabens! o número {a} está dentro da lista.')
else:
    print(f'Infelizmente o número {a} não está na lista.')