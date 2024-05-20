def palin(a):
    lis = []
    li = []
    for i in a:
        lis.append(i)
    for v in lis[::-1]:
        li.append(v)
    if li == lis:
        return True
    else:
        return False


pa = str(input('digite a frase/palavra: ')).strip().upper().replace(' ','')
r = palin(pa)
print(f'A palavra é um palíndromo: {r}')