import numpy as np 

a = np.arange(10)
print ("Actual array is :\n",a)
s = slice(2,7,2) 
print (a[s])

a = np.arange(20) 
b = a[2:17:2] 
print (b)

a = np.arange(10) 
b = a[2:7:2] 
print (b)
