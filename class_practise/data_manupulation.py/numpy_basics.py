import numpy as np

#create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:",arr)

#create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2d)


zeros = np.zeros((2, 3))
print("Zeros Array:\n", zeros)
ones = np.ones((3, 3))
print("Ones Array:\n", ones)
identity = np.eye(3)
print("Identity Matrix:\n", identity)
sequence = np.arange(0, 10, 2)
print("Sequence Array:", sequence)
linspace = np.linspace(0, 1, 5)
print("Linspace Array:", linspace)

print(arr.shape)
print(arr2d.shape)
print(arr.ndim)
print(arr2d.ndim)
print(arr.dtype)
print(arr2d.dtype)

print(arr.mean())
print(arr2d.mean())

print(arr.size)
print(arr2d.size)