def juntar(a, b):
    for i in a:
        if i not in tudo:
            tudo.append(i)
    for i in b:
        if i not in tudo:
            tudo.append(i)
    print(tudo)

tudo = []
a1 = [1,3,5,7,9,13,23,45,2,1]
a2 = [2,4,6,8,12,19,1]
juntar(a1,a2)
