"""5.WAP FOR SAVING AND LOADING ARRAYS"""
import numpy as np

a = np.array([10, 20, 30, 40, 50])

# Saving array
np.save("data.npy", a)

# Loading array
b = np.load("data.npy")

print("Loaded Array:", b)
