emp = [
    {'nome': 'Luis', 'cargo': 'gestor', 'salário': 1900},
    {'nome': 'Aradou', 'cargo': 'supervisor', 'salário': 2000},
    {'nome': 'Gus', 'cargo': 'limpeza', 'salário': 2200},
    {'nome': 'jean', 'cargo': 'executivo', 'salário': 3000}
]

emp.append({'nome': 'jully', 'cargo':'chefe', 'salário': 2000})

emp[0]['salário'] = 3000

for i in emp:
    print(i)

print('------------------------')
salatot = 0
for i in emp:
    salatot += i['salário']

print(f'O salário total da empresa é \033[31m{salatot}\033[m')

