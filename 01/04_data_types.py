# NumPy Data Types
# Purpose: Understand data types in NumPy arrays

import numpy as np

# 1. Integer array
int_arr = np.array([10, 20, 30, 40])
print("Integer array:", int_arr)
print("Data type:", int_arr.dtype)

# 2. Float array
float_arr = np.array([10.5, 20.2, 30.8])
print("\nFloat array:", float_arr)
print("Data type:", float_arr.dtype)

# 3. String array
str_arr = np.array(["Python", "NumPy", "AI"])
print("\nString array:", str_arr)
print("Data type:", str_arr.dtype)

# 4. Specify a data type
arr = np.array([1, 2, 3, 4], dtype=float)
print("\nFloat conversion:", arr)
print("Data type:", arr.dtype)
