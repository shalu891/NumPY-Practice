# astype - change the data type of an array
import numpy as np

arr = np.array([1.2, 2.5, 3.7, 4.1])
print(arr.dype)

# Convert float array to integer array
int_arr = arr.astype(int) 
print(int_arr) 
print(int_arr.dtype) 