def mdc(z,x,y):
    for i in range(z + x):
        if i != 0:
            if z % i == 0:
                if x % i == 0:
                    if y % i == 0:
                        l.append(i)
        l.sort(reverse=True)


a = int(input('n1: '))
b = int(input('n2: '))
c = int(input('n3: '))
l = []
r = mdc(a,b,c)
print(f'O mdc dos números apresentados é {l[0]}')