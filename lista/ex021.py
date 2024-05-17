def anagran(z, x):
    li = []
    lis = []
    for i in z:
        for v in i:
            li.append(v)
    for i in x:
        for v in i:
            lis.append(v)
    li.sort()
    lis.sort()
    if lis == li:
        if len(lis) == len(li):
            return True
        else:
            return False
    else:
        return False
    
            
    


a = str(input('1: ')).strip().upper()
b = str(input('2: ')).strip().upper()
resp = anagran(a, b)
print(resp)
