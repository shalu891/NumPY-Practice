
# NumPy Array Reshaping
# Purpose: Change the shape of an array

import numpy as np

# 1. Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

print("Original array:", arr)
print("Original shape:", arr.shape)

# 2. Reshape into a 2D array
reshaped_arr = arr.reshape(2, 3)

print("\nReshaped array (2 rows, 3 columns):")
print(reshaped_arr)
print("New shape:", reshaped_arr.shape)

# 3. Reshape into another structure
reshaped_arr2 = arr.reshape(3, 2)

print("\nReshaped array (3 rows, 2 columns):")
print(reshaped_arr2)
print("New shape:", reshaped_arr2.shape)
