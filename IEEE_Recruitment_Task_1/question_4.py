import numpy as np

# Using the same matrix as question 3
array = np.random.randint(2, 100, size=(5, 5))
print(array)

# Slice the 5x5 matrix to get an inner 3x3 matrix
mid = array[1:4, 1:4]
print(mid)

# Taking the first row and last column separately
row = mid[0]
col = mid[:, -1]

# Displaying dot product of the two
product = row.dot(col)
print(f"Dot product of first row and last column of inner 3x3 matrix is {product}")
