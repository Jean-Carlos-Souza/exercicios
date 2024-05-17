def encontrar(a, b):
    r = a.count(b)
    return r

encon = str(input('Qual caractere deseja encontrar: '))
string = str(input('String: '))
resp = encontrar(string, encon)
print(f'A caractere {encon} foi achada {resp} vezes na string // {string} //')

