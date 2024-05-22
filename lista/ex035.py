def inte(b):
    for i in range(b):
        if i != 0:
            if b % i == 0:
                lis.append(i)


lis = []
a = int(input('Numero inteiro: '))
inte(a)
print(lis)