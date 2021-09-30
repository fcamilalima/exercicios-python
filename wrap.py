def wrap(filename, width):
    f=open(filename).read().split('\n')
    g=f[::-1]
    h=[]
    for i in g:
        if len(i)>width:
            print(i[0:width])
            print(i[width:])
            h.append(i)
            
    return h

wrap('she.txt', 30)
