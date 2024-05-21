def interface():
    a = 'BEM VINDO'
    print('-' * 35)
    print(f'|{a:^33}|')
    print('-' * 35)
def linha():
    print('-' * 35)
def con(a, b):
    if a == 1:
        a1 = b * 5
        return a1
    if a == 2:
        return b
    if a == 3:
        return b * 3.5

interface()
din = int(input('Quanto deseja converter: '))
linha()
print('DOLAR    [1] \nREAL     [2] \nJAPANES  [3] ')
c = int(input('Para qual deseja converter: '))
res = con(c, din)
linha()
print(f'O total depois da conversão é [{res}]')