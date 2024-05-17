def dici(b):
    for i in b:
        di = {
            i:len(i)
        }
        dados.append(di)

dados = []
di = {}
a = str('Escreva uma função que recebe uma string de texto e retorna um dicionário onde as chaves são palavras e os valores são a contagem').split()
dici(a)
print(dados)