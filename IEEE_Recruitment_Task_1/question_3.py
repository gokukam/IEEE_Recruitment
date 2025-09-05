import numpy as np

# Create the array with random values in specified range
array = np.random.randint(2, 100, size=(5, 5))

# Display the array and it's max, min and mean
print(array)
print(f"Maximum: {np.max(array)}")
print(f"Minimum: {np.min(array)}")
print(f"Mean: {np.mean(array)}")

# Normalize values to range of 0-1 (using deviation from min and range of values)
norm_array = (array - np.min(array)) / (np.max(array) - np.min(array))

# Flatten the matrix to a 1D array using .ravel()
flattened = norm_array.ravel()

# Print the sorted flattened array
print(sorted(flattened))
