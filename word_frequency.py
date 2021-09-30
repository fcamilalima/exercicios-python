lista = {}

def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency


def read_words(filename):
    return open(filename).read().split()


def main(filename):
    print(filename)
    frequency = word_frequency(read_words(filename))
    f = frequency
    for word, count in frequency.items():
        
        print(word, count)

    while len(f.items()) > 0:
        valor = max(f.values())
        chave = max(f, key=lambda key: f[key])
        del f['{}'.format(chave)]
        lista.setdefault(chave, valor)


#    print(f)
#    print(lista)


if __name__ == "__main__":
    import sys

    param = sys.argv[1]
    main(param)
