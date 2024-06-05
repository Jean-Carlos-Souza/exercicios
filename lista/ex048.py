def encontrar():
    c = 0
    for i in lista_frutas:
        if i == 'banana':
            dic['banana'] += 1
        if i == 'maça':
            dic['maça'] += 1
        if i == 'morango':
            dic['morango'] += 1


lista_frutas = ['banana', 'banana', 'banana', 'maça', 'maça', 'morango']
dic = {
    'banana': 0,
    'maça': 0,
    'morango': 0
}

encontrar()

print(dic)