def triplets(n):
    return print([(x, y, x+y) for x in range(1,n) for y in range(1,n) if x+y<=n]) 

triplets(4)
