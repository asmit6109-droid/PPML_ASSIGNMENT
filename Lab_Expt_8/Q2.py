"""2.WAP FOR DATA TYPES AND STRUCTURES IN NUMPY"""
import numpy as np

# Data Types
a = np.array([1, 2, 3], dtype=int)
b = np.array([1.5, 2.5], dtype=float)

print(a, a.dtype)
print(b, b.dtype)

# Data Structures
x = np.array([1, 2, 3])          
y = np.array([[1, 2], [3, 4]])  

print(x)
print(y)
