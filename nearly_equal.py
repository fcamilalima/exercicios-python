resposta = []
retorno = False

def nearly_equal(str1, str2):
    contador = 0
    str1_list = list(str1)
    str2_list = list(str2)
#    for i in str2_list:
    for j in str1_list:
        if str2.find(j) != -1:
            contador += 1
#            print('i = {}'.format(i))
            print('j = {}'.format(j))
            print('contador = {}'.format(contador))
            print('Tamanho da string de pesquisa = {}'.format(str1_list))

        if contador == len(str1_list)-1:
            retorno = True
            return True
            break
        else:
            retorno = False

    return retorno

print(nearly_equal('man', 'woman'))
