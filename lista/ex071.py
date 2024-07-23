num = int(input('Digite um numero: '))
lista = []

for i in range(1, num + 1, 1):
    lista.append(i)

print(lista)

c = 0
while c < len(lista):
    if lista[c] % 3 == 0:
        print(lista[c])
    c += 1
