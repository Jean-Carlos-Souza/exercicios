def pala():
    while True:
        li.append(str(input('NOme: ')))
        r = str(input('Quer continuar: '))
        if r == 'n':
            break
    for i in li:
        npa.append(len(i))
    
    
li = []
npa = []
pala()
for i in npa:
    print(i)
