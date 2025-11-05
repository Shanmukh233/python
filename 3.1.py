import numpy as np
# Create arrays
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])

print("Add:", np.add(a, b))

print("All non-zero:", np.all(a))

print("Greater:", np.greater(a, b))
print("Greater or equal:", np.greater_equal(a, b))
print("Less:", np.less(a, b))
print("Less or equal:", np.less_equal(a, b))
print("Equal:", np.equal(a, b))
print("All close (tolerance):", np.allclose(a, b))

print("Info:", np.info(np.add))
print("Zeros:", np.zeros(5))
print("Ones:", np.ones(5))
print("Linspace:", np.linspace(0, 10, 5))
print("To list:", a.tolist())
