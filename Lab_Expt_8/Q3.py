"""3.WAP FOR NUMPY ARRAY PROPERTIES AND FUNCTIONS"""
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:", a)
print("Shape:", a.shape)
print("Size:", a.size)
print("Dimension:", a.ndim)
print("Data Type:", a.dtype)

print("Sum:", np.sum(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Mean:", np.mean(a))
