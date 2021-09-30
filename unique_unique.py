def unique(x):
    x1=[]
    for i in range(0,len(x)):
        aux=x[i]
        if x[i].islower():
            x1.append(aux)
    print(x)
    print(x1)
    return x1

j = ['python', 'java', 'Python', 'Java']
unique(j)
