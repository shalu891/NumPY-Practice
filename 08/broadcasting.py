
# NumPy Broadcasting
# Purpose: Perform operations between arrays and single values

import numpy as np

# 1. Create a NumPy array
arr = np.array([10, 20, 30, 40])

print("Original array:", arr)

# 2. Add a single number to every element
print("\nAdd 5:", arr + 5)

# 3. Multiply every element by 2
print("Multiply by 2:", arr * 2)

# 4. Broadcasting with two arrays of compatible shapes
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])

print("\nArray a:")
print(a)

print("\nArray b:")
print(b)

print("\nBroadcasting result:")
print(a + b)
