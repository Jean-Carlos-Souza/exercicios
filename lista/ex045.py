lista_impares = []

inteiro = int(input('Escreva um número inteiro que deseja: '))
for i in range(1, inteiro+1):
    if i % 2 == 1:
        lista_impares.append(i)
print(lista_impares)
