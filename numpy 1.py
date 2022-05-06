'''
import numpy
#simple code
a=numpy.array([1,52,6,10])
print("The elements are:", a)

b=numpy.array([[1,2,3,6],[3,6,5,8],[9,8,6,65]])
print("The array is:\n", b)
print("----------------***********    END OF PROG-1    *************----------------")

n=int(input("Enter the value of n:-"))
print("The second index position set of elements are:", b[n])

#USING NDMIN Specifies minimum dimensions of resultant array
import numpy as np 

a = np.array([1, 2, 3,4,5], ndmin = 5) 
print (a)

a = np.array([1, 2, 3], dtype = complex) 
print (a)


#creating an array from sub classes 'MAT'
import numpy as np
a=np.array(np.mat('1 2; 3 4;3 9;9 78;1 2 '))
print (a)
'''
#creating list of array with zeros &  ones
import numpy as np
a=np.zeros(5)
b=np.ones(10)
print (a,"\n",b)

c=np.zeros((5,), dtype=np.complex)
print (c)
'''
import numpy as np
a=np.ones([2,6],dtype='complex')
print(a)
'''

'''
import numpy as np
s = (2,2)
a=np.zeros(s)
print (a)
'''
'''
import numpy as np
x = np.empty([9,7], dtype = int) 
print (x)
'''
