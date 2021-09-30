def unique(x1):
    x2=set(x1)
    x3=[]
    for i in x2:
        if x1.count(i)==1:
            x3.append(i)
    return x3

k=[]
k=unique([1, 2, 1, 3, 2, 5])
print("Número únicos é(são) s", k)
