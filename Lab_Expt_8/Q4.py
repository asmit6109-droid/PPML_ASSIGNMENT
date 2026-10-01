"""4.WAP FOR STATISTICAL OPERATIONS AND BROADCASTING ON ARRAYS"""
import numpy as np

a = np.array([10, 20, 30, 40])

# Statistical operations
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard Deviation:", np.std(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))

# Broadcasting
b = a + 5
print("After Broadcasting:", b)
