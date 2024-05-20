def media(lista):
    l = len(lista)
    print(l)
    if l % 2 == 0:
        for i in lista(0, l/2):
            print(i)

nu = []
num = []
while True:
    a = int(input('Numero: '))
    if a not in num:
        num.append(num)
    while True:
        r = str(input('Quer Continuar: s/n ')).strip().upper()
        if r in 'SN':
            break
    if r == 'N':
        break
media(num)