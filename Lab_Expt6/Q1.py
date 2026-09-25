"""Q1.WAP TO PRINT A MATRIX CONTAINING GROUP OF SIMILAR ELEMENTS BY GIVING THE INPUT RAND0OMLY IN ANOTHER MATRIX"""
import random

def group(a):
    for x in set(sum(a, [])):
        print(x, ":", [i for row in a for i in row if i == x])

r, c = 3, 3
a = [[random.randint(1, 5) for j in range(c)] for i in range(r)]

print("Matrix:")
for row in a:
    print(row)

print("Groups:")
group(a)