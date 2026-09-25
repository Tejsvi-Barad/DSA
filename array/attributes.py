import numpy as np

a=np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(a.ndim)       # => Number of dimensions
print(a.shape)      # => 2 rows and 5 columns
print(a.size)       # => Total number of elements
print(a.itemsize)   # => Each int64 element uses 8 bytes
print(a.dtype)      # => Data type of elements
print(a.nbytes)     # => Total memory used: 10 × 8 = 80 bytes
