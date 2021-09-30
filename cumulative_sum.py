def cumulative_sum(h):
    a=len(h)
    b=0
    c=[0, 0, 0, 0]
    for i in range(0, a):
        b=i
        aux=0
        while b>=0:
            print('b=', b)
            aux+=h[b]
            b-=1
            print('aux=',aux)
        c[i]=aux
        print('c[',i, ']=',c[i])
    print(c, h)
    return c


cumulative_sum([4, 3, 2, 1])

            

        
        
        
            
