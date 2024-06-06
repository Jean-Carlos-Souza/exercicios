def me():
    r = []
    for k, v in lista_es.items():
        if v >= 7:
            r.append(k)
            r.append(v)
    return r



lista_es = {
    'aluno1':7, 'aluno2':2, 'aluno3':8, 'aluno4':9, 'aluno5':3
}
resp = []
resp.append(me())
for i in resp:
    for v in i:
        print(v)

