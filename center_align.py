def wrap(filename):
    f=open(filename).read().split('\n')
    for i in f:
        print(i.center(60, ' '))
    return f

wrap('she.txt')
