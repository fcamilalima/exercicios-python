def group(x):
    list=x[0]
    size=x[1]
    print(x[0])
    print(x[1])
    y=[]
    
    y=[list[i:i+size] for i in range(0, len(list), size)]

    return y

k=group([[1, 2, 3, 4, 5, 6, 7, 8, 9], 3])
print(k)



