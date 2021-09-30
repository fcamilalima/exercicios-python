def reverse(filename):
    f =open(filename).read().split('\n')
    g=f[::-1]
    for i in g:
        print(i)
    return g

reverse('she.txt')
