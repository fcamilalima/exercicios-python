def grep(filename, key):
    f=open(filename).read().split('\n')
    g=[]
    for i in f:
        if key in i:
            print(i)
            g.append(i)
    return g

grep('she.txt', 'sure')
