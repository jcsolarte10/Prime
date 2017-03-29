def primos():
 i = 0
 prim = []
 b=0
 for i in range(100000):
     es = True
     if i>2 :
         a = 2
         while a < len(prim) and es == True:
             temp = i%prim[a]
             if temp == 0:
                 es = False
             a=a+1            
                          
     if es:
      prim.append(i)

     i=i+1
         
 return prim

def esPrimo(valor):
    num = []
    num = primos()
    es = True

    if num.count(valor)==0:
        es = False

    return es
