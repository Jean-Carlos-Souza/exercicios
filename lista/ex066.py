

lista = []
lista_media = []
di = {}
c = 0
for i in range(0, 5):
    c += 1
    a = str(input('Nome do Aluno: '))
    b = float(input('Nota do Aluno: '))
    di[a] = a
    di[b] = b
    print(di)

print(di.values())

