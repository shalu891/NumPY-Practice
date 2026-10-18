#creation of an array using numpy
import numpy as np

# 1. create from python list
#syntax = np.array([ele1, ele2, ele3, ...])
arr1 = np.array([10, 20, 30, 40]) 
print(arr1)

# 2.create an  array of zeroes
# syntax = np.zeros((rows, columns))
arr2 = np.zeros((2, 3))
print(arr2)

# 3.create an array of ones
# syntax = np.ones((rows, columns)) 
arr3 = np.ones((2, 3))
print(arr3)

# 4.create an array of a specific value
# syntax = np.full((rows, columns), value)  
arr4 = np.full((2, 3), 7)
print(arr4) 

# 5.create an array with a range of  values 
# syntax = np.arange(start, stop, step)
arr5 = np.arange(0, 10, 2)
print(arr5)

# 6. create evenly  spaced values
# syntax = np.linspace(start, stop, num)
arr6 = np.linspace(0, 1, 5)
print(arr6) 

# 7. create an identity matrix
# syntax = np.eye(n)    
arr7 = np.eye(3)
print(arr7)

# 8. create an  empty array
# syntax = np.empty((rows, columns))
arr8 = np.empty((2, 3))
print(arr8)
