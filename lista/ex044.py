def par():
    for i in lista_inteiros:
        if i % 2 == 0:
            lista_par.append(i)
        

lista_par = []
lista_inteiros = []

for i in range(1, 11):
    lista_inteiros.append(i)

par()

for i in lista_par:
    print(i)