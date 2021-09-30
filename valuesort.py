from operator import itemgetter
def valuesort(listas):
    print(sorted(listas.items(), key = itemgetter(1), reverse=True))
    return listas

valuesort({'x':1, 'y':2, 'z':3})
    
