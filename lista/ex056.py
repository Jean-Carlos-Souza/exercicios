n = int(input('Numero inteiro: '))
s = 1
for i in range(n, 1, -1):
    s *= i
    print(s)