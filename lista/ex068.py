notas = [
    {'aluno': 'Jean', 'nota1': 10, 'nota2': 3},
    {'aluno': 'Luan', 'nota1': 6, 'nota2': 8},
    {'aluno': 'Beto', 'nota1': 7, 'nota2': 4},
    {'aluno': 'Ana' , 'nota1': 3, 'nota2': 6},
    {'aluno': 'luiza', 'nota1': 8, 'nota2': 8},
]

notas.append({'aluno': 'Jully', 'nota1': 3, 'nota2': 9})

notas[2]['nota1'] = 7

print('--------------------------')

for i in notas:
    print(i)
    print('--------------------------')

for media in notas:
    media_total = (media['nota1'] + media['nota2']) / 2
    print(f'O aluno(a) {media['aluno']} tem média de {media_total}')
    print('--------------------------')
