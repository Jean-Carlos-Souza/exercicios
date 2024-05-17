def media(num):
    s = 0
    for i in num:
        s += i
    m = s / len(num)
    return m
    


nu = [1,2,3,4,56,78,34]
me = media(nu)
print(f'a média da lista {nu} é: {me:.2f}')
