def parse(filename, str1, str2):
    i = []

    f = open(filename).read().split('\n')
    print([i.replace(str(str1), str(str2)).split(',') for i in f])

    return f


parse('a.txt', '!', ',')
