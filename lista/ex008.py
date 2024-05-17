def contar(a):
    con = len(a)
    return con


s = str(input('Escreva a string: ')).strip().replace(' ', '')
r = contar(s)
print(f'A string apresentada contem {r} caracteres')