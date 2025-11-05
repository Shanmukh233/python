import numpy as np

# Create a sample NumPy array
arr = np.array([3, 7, 2, 9, 4, 7, 2, 9, 3])

print("Original Array:", arr)
print("Representation using repr():", repr(arr))

# a) Extract all numbers less than and greater than a specified number
num = 5
less_than = arr[arr < num]
greater_than = arr[arr > num]

print("\nNumbers less than", num, ":", less_than)
print("Numbers greater than", num, ":", greater_than)

# Count occurrences of a specific number using count_nonzero
count_7 = np.count_nonzero(arr == 7)
print("Count of number 7:", count_7)

# Count of all unique elements using bincount
print("\nBincount (frequency of numbers):", np.bincount(arr))
print("Unique elements and their counts:", np.unique(arr, return_counts=True))

# b) Find indices of max and min numbers along a given axis
matrix = np.array([[1, 5, 2],
                   [9, 3, 7],
                   [4, 6, 8]])

print("\nMatrix:\n", matrix)

# Maximum and minimum values
print("Max value:", np.max(matrix))
print("Min value:", np.min(matrix))

# Indices of max and min
print("Index of max (flattened):", np.argmax(matrix))
print("Index of min (flattened):", np.argmin(matrix))

# Along axis 0 (columns)
print("Indices of max along axis 0:", np.argmax(matrix, axis=0))
print("Indices of min along axis 0:", np.argmin(matrix, axis=0))

# Along axis 1 (rows)
print("Indices of max along axis 1:", np.argmax(matrix, axis=1))
print("Indices of min along axis 1:", np.argmin(matrix, axis=1))
