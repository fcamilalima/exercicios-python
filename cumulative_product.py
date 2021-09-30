def cumulative_product(h):
    a=len(h)
    b=0
    c=[1, 1, 1, 1]
    for i in range(0, a):
        b=i
        aux=1
        while b>=0:
            print('b=', b)
            aux*=h[b]
            b-=1
            print('aux=',aux)
        c[i]=aux
        print('c[',i, ']=',c[i])
    print(c, h)
    return c


cumulative_product([1, 2, 3, 4])

            

        
        
        
            
