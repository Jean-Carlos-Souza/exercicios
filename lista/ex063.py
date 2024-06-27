def ocorrencia(lista):
    dicc = {}
    lis = []
    for i in lista:
        dicc['chave'] = i
        dicc['valor'] = 1
        if i == dicc['chave']:
            dicc['valor'] = dicc['valor'] + 1

        lis.append(dicc)
        return lis
        



lista = ['bola', 'bola', 'sorvete', 'siri', 'siri', 'jogo']
dic = ocorrencia(lista)
print(dic)