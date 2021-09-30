
def extsort(x):
    list1=[]
    list2=[]
    list_22=[]
    list_222=[]
    list3=[]
    list4=[]
    list5=[]
    cont=0
    
    for i in x:
        list1.append(i.split('.'))
    print(list1)
        
    for j in range(0,len(list1)):
        list2.append(list1[j][1])
        list2.sort()
        list_22=set(list2)
        list_222=sorted(list_22)    
    print(list2)
    print(list_22)
    print(list_222)
 
    for k in range(0, len(list_222)):
        aux = "".join([".", list_222[k]])
        list3.append(aux)
    print(list3)
        
    for m in list3:
        for n in x:
            if n.count(m)==1:
                list4.append(n)
                
    for o in list4:
        if cont%2==0:
            list5.append(o)
            cont+=1
        

    return list4

print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))

                
                
        
#k=extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
#print(k)
