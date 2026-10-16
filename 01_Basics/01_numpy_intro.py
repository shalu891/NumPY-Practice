import numpy as np

# 1. Numpy version
print(np.__version__)

# 2. create an array
arr = np.array([10, 20, 30, 40, 50])

# 3. array information
print(arr)
print(type(arr))
print(arr.ndim)
print(arr.size)
print(arr.dtype)

# 4. array operations (practise)
print(arr * 2)
print(arr + 10)

# 5. comparison
print(arr > 25)