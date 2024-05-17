def contate(a, b):
    for i in a:
        for v in b:
            if i == v:
                if v not in nu3:
                    nu3.append(v)

nu3 = []
nu1 = [1,2,3,4,5,34,56,23,46,67,23,56,4]
nu2 = [1,2,3,4,5,6453,423,23,3,46,54,53,45,3,56]
contate(nu1, nu2)
nu3.sort()
print(nu3)