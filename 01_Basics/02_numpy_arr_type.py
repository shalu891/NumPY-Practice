# NumPy Arrays
# Purpose: Understand 1D, 2D, and 3D NumPy arrays or  type  of ndarrays

import numpy as np

# 1. One-Dimensional Array (1D)
arr1 = np.array([85, 90, 72, 88])

print("1D Array:", arr1)
print("Dimensions:", arr1.ndim)


# 2. Two-Dimensional Array (2D)
arr2 = np.array([[85, 90],
                 [72, 88]])

print("2D Array:")
print(arr2)
print("Dimensions:", arr2.ndim)


# 3. Three-Dimensional Array (3D)
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("3D Array:")
print(arr3)
print("Dimensions:", arr3.ndim)



# Practice 1: Identify dimensions
arr1 = np.array([10, 20, 30])
arr2 = np.array([[10, 20], [30, 40]])
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("arr1 dimensions:", arr1.ndim)
print("arr2 dimensions:", arr2.ndim)
print("arr3 dimensions:", arr3.ndim)