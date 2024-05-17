def reverso(a):
    re = []
    for i in a[::-1]:
        re.append(i)
    return re
        


minha_lista_reversa = []
minha_lista = []
while True:
    a = int(input('Digite um número: '))
    if a in minha_lista:
        print('Número já está alocado dentro da lista!')
    else:
        minha_lista.append(a)
    res = str(input('Quer Continuar: S/N ')).strip().upper()
    while True:
        if res in 'SN':
            break
    if res == 'N':
        break
minha_lista_reversa = reverso(minha_lista)
for i in minha_lista_reversa:
    print(i,'...',end='')
print()

