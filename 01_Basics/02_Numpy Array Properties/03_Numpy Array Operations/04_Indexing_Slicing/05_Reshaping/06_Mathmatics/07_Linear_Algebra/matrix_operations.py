
# NumPy Linear Algebra
# Purpose: Perform basic matrix operations

import numpy as np

# 1. Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# 2. Matrix addition
print("\nMatrix Addition:")
print(A + B)

# 3. Matrix multiplication (element-wise)
print("\nElement-wise Multiplication:")
print(A * B)

# 4. Matrix multiplication
print("\nMatrix Product:")
print(np.dot(A, B))

# 5. Transpose of a matrix
print("\nTranspose of A:")
print(A.T)

# 6. Determinant of a matrix
print("\nDeterminant of A:")
print(np.linalg.det(A))
