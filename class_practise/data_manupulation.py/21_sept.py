import numpy as np
"""Saving One Array"""
# a = np.array([5,10,15,20,25])
# np.save("my_array.npy",a)
# data = np.load("my_array.npy")
# print(data)
"""Saves Multiple Array"""
# b = np.array([1,2,3])
# c = np.array([4,5,6])
# np.savez("data.npz",first=b, second=c )
# data = np.load("data.npz")
# print(data["first"])
# print(data["second"])
"""Matrix Multiplication"""
# print(np.dot(b,c))
# e = np.random.randint(21,87,(3,4))
# f = np.random.randint(12,99,(4,5))
# print(np.dot(e,f))
"""Solving A Linear Eqn Ax = b"""
# g = np.array([[1,2,1],[2,1,1],[1,1,2]])
# h = np.array([8,7,9])
# x = np.linalg.solve(g,h)
# print(x)

"""Image Processing Using NumPY"""
image_rgb = np.zeros((100, 100, 3), dtype=np.uint8)

image_rgb[25:75, 25:75] = [255, 255, 255]

# CONVERT RGB TO GRAYSCALE
# Shape changes from (100,100,3) to (100,100)

luma_weights = np.array([0.2989, 0.5870, 0.1140])

gray_image = np.dot(
    image_rgb[..., :3],
    luma_weights
).astype(np.float32)


# Define a 3x3 Sobel horizontal edge detection kernel

sobel_horizontal = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])


# Apply 2D convolution manually

height, width = gray_image.shape

output = np.zeros((height - 2, width - 2), dtype=np.float32)

for i in range(height - 2):
    for j in range(width - 2):

        region = gray_image[i:i+3, j:j+3]

        output[i, j] = np.sum(region * sobel_horizontal)


# Display some information

print("RGB Image Shape:", image_rgb.shape)
print("Gray Image Shape:", gray_image.shape)
print("Output Shape:", output.shape)
print("Maximum Edge Value:", output.max())
print("Minimum Edge Value:", output.min())