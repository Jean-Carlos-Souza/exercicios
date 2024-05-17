def par(n):
    for i in range(n-n, n+1):
        if i % 2 == 0:
            lis_par.append(i)
        

lis_par = []
p = int(input('Número: '))
par(p)
print(lis_par)