def soma(lista):
    s = 0
    for i in lista:
        s += i
    return s


lis = [1, 3, 5, 3, 10]
res = soma(lis)
print(res)