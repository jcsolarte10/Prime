import numpy as np
def primos(r):
    dir ="info.gz" 
    try:
        prim = np.array(np.loadtxt(dir),dtype=int)
    except FileNotFoundError:
        print ("Se creará nuevo archivo.")
        ans= input("Should we proceed?(y/n)")
        if ans == "y":
            prim = np.array([1,2])
        else:
            return None
        
            
        
    for i in range(prim[-1],prim[-1]+r):
        es = True
        temp = sum(i%prim[1:]==0)   
	               
        if temp==0:
            prim = np.append(prim,i)
            
    np.savetxt(dir,prim,delimiter=",")     
    return prim[-1]

