def parse_csv(filename):
    f = open(filename).read().split()
    return print([[i.split(',')] for i in f])


parse_csv('a.csv')
