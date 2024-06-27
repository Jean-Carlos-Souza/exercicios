def remover_duplicada(lis):
    l = []
    for i in lis:
        if i not in l:
            l.append(i)
    return l


lista = [1,2,2,3,3,4,4,5,5,6,6]
lis = remover_duplicada(lista)
print(lista)
print(lis)