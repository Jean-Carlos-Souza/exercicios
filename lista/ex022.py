def cons(n):
    for i in n:
        if i not in nu:
            nu.append(i)
    


nu = []
num = []
while True:
    a = int(input('Numero: '))
    num.append(a)
    r = str(input('Deseja continuar: s/n ')).strip().upper()
    if r == 'N':
        break
cons(num)
print(num)
print(nu)