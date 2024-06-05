def media():
    s = 0
    for i, v in dic.items():
        for valor in v:
            s += valor
        s = s/len(v)
        listaa.append(s)
        s = 0
        if i == 'A':
            dic['A'] = listaa[0]
        if i == 'B':
            dic['B'] = listaa[0]
        if i == 'C':
            dic['C'] = listaa[0]
        listaa.clear()


dic = {'A': [1,2,3], 'B': [4,5,6], 'C': [7,8,9] }
print(dic)
listaa = []
media()
print(dic)