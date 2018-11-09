import numpy as np

def multiplicar(a,b):
  if len(a[0,:]!=len(b[:,0]):
         print "Operacion no se puede realizar"
  else:
         res=np.zeros((len(a[:,0]),len(b[0,:])))
         for i in range(0,len(a[:,o])):
              for j in range(0,len(b[o,:])):
                  for k in range(0,len(a[o,:])):
                      res[i][j]+=a[i][k]*b[k][j]
         return res
  return 0
         
         
a=np.array(([3,2,1],[4,2,3],[5,2,1]))
e=np.array(([-24,18,5],[20,-15,-4],[-5,4,1]))
multiplicar(a,e)

