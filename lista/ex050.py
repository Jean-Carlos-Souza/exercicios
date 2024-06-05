def contar(n):
    s = 0
    for i in range(1, n+1, 2):
        s += i
    return s

n = int(input('Digite um número inteiro positivo: '))

s = contar(n)
print(f'A soma de todos os números impares até {n} é: {s}')