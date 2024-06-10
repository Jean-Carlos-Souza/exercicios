from random import randint
lista = []
for i in range(0,10):
    lista.append(randint(1, 100))

s = 0
for i in lista:
    s += i
 
a = s / len(lista)
print(lista)
print(f'A soma de todos os números da lista é {s}')
print(f'A média da lista é {a}')