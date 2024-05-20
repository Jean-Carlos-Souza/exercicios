def media(b, c, d):
    s = (b + c + d) / 3
    return s

a1 = int(input('Nota1: '))
a2 = int(input('Nota2: '))
a3 = int(input('Nota3: '))
a = media(a1, a2, a3)
print(f'A média entre as notas [{a1}] - [{a2}] - [{a3}] é [{a:.2f}] de \033[4mmédia\033[m')
