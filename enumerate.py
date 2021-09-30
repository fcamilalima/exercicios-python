def enumerate(x):
    return [(i,v) for i, v in zip(range(0,len(x)),x)]

print(enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
