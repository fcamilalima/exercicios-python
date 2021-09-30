n=int(input('Digite um número para calcular seu fatorial:'))
c = 0
f = 1
for c in range(1, n+1):
    f*=c
print('O fatorial de {} é {}.'.format(n,f))
