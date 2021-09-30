def invertdict(listas):
    chaves = listas.keys()
    valores = listas.values()
    print('Chaves = {}'.format(chaves))
    print('Valores = {}'.format(valores))
    lista_nova = {}
    for chave, valor in listas.items():
        lista_nova['{}'.format(valor)] = chave
    return lista_nova

print(invertdict({'x':1, 'y':2, 'z':3}))