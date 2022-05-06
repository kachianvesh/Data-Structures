# Python program to demonstrate sorting in numpy 
import numpy as np 
  
a = np.array([[1, 4, 2], 
            [3, 4, 6], 
            [0, -1, 5]]) 
  
# sorted array 
print ("Array elements in sorted order:\n",np.sort(a, axis = None)) 
  
# sort array row-wise 
print ("Row-wise sorted array:\n", np.sort(a, axis = 1)) 

# specify sort algorithm 
print ("Column wise sort by applying merge-sort:\n",np.sort(a, axis = 0, kind = 'mergesort')) 
