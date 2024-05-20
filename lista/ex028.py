def fa(a):
    t = (a - 32) / 1.8
    return t
def ce(a):
    r = 1.8 * a + 32
    return r

a = str(input('Quer converter para qual temperatura: f/c --> '))
if a == 'c':
    temp = float(input('Qual a temperatura: '))
    ce = fa(temp)
    print(f'A temperatura [{temp}] em Celsius é [{ce:.2f}]')
else:
    tem = float(input('Qual a temperatura: '))
    far = ce(tem)
    print(f'A temperatura [{tem}] em fahrenheit é [{far:.2f}]')
