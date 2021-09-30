a = {'x': 1, 'y': 2, 'z': 3}
chaves = []
valores = []
lista = {}
del a['z']
print('Lista a `{}:'.format(a))
a.setdefault('z', 3)
print('Lista a: {}.'.format(a))
print('Chaves: {}.'.format(a.keys()))
print('Valores: {}.'.format(a.values()))
print('Items: {}.'.format(a.items()))
print('Maior Item: {}'.format(max(a.items())))
chaves = max(a.keys())
valores = max(a.values())
lista = {'{}'.format(chaves): valores}
print("Chave máxima = {}".format(chaves))
print("Valores máxima = {}".format(valores))
print("Lista ordenada = {}".format(lista))
del a['{}'.format(chaves)]
print("A = {}".format(a))



