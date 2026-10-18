import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])


# shape - number of rows and colomns 
print("Shape:", arr.shape)  

# 4. Data type of elements
print("Data type:", arr.dtype)

# 5. Number of bytes per element
print("Item size:", arr.itemsize)

# 6. Total memory used by array
print("Total bytes:", arr.nbytes)


