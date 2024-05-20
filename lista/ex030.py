a = str(input('palavra: ')).strip().lower()
a1 = a.count('a')
a2 = a.count('e')
a3 = a.count('i')
a4 = a.count('o')
a5 = a.count('u')
s = a1 + a2 + a3 + a4 + a5
print(f'A soma de todas as vogais são ao todo: {s}')