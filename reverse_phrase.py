def reverse_phrase(filename):
    f=open(filename).read().split('\n')
    g=[]
    for i in f:
        g.append(i[::-1])
        print(i[::-1])
    return g

reverse_phrase('she.txt')
