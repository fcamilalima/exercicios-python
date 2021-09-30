l = []
repetidos = []
lista = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
def anagram(listas):
    for i in range(0, len(listas)):
        for j in range(i+1, len(listas)):
            if mutate(listas[i], listas[j]):
                l.append(listas[i])
                l.append(listas[j])
    return l

def mutate(str1, str2):
    contador = 0
    str1_list = list(str1)
    str2_list = list(str2)
    # for i in str2_list:
    for j in str1_list:
        if str2.find(j) != -1:
            contador += 1
            # print('i = {}'.format(i))
            # print('j = {}'.format(j))
            # print('contador = {}'.format(contador))
            # print('Tamanho da string de pesquisa = {}'.format(str1_list))

        if contador == len(str1_list):
            retorno = True
            return True
            break
        else:
            retorno = False

    return retorno


def remove_repetidos(lis):
    j = 0
    while j <= len(lis)-1:
        aux = lis[j]
#        print(aux)
#        print(lis.count(aux))
        if lis.count(aux) >= 2:
            del lis[j]
        else:
            j += 1
    return lis

def compara(lista1, lista2):
    for i in lista2:
#        print(lista1.count(i))
        if lista1.count(i) == 0:
            lista1.append(i)
#        print(i)
#        print(lista1)
#        print(lista2)

    return lista1




print(compara(remove_repetidos(anagram(lista)), lista))

