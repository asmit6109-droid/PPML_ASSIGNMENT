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

"""Q2.WAP TO PRINT A MATRIX ALONG WITH SUMMATION OF ROW ELEMENTS AND COLUMN ELEMENTS AFTER ENTERING 3*3 MATRIX"""
def matrix_sum(a):
    for row in a:
        print(row, "Sum =", sum(row))

    print("Column Sums:")
    for j in range(3):
        print(sum(a[i][j] for i in range(3)))

a = []
for i in range(3):
    a.append(list(map(int, input("Enter 3 elements: ").split())))

print("Matrix and Row Sums:")
matrix_sum(a)

"""Q3.WAP TO PRINT THE TRANSPOSE OF A MATRIX OF N*N ORDER"""
def transpose(a):
    for j in range(n):
        print([a[i][j] for i in range(n)])

n = int(input("Enter N: "))
a = [list(map(int, input().split())) for i in range(n)]

print("Transpose:")
transpose(a)

"""Q4.WAP TO CHECK IF A VALUE IS PRESENT IN THE LIST OR NOT,USING LAMBDA FUNCTION."""
a = list(map(int, input("Enter list: ").split()))
x = int(input("Enter value: "))

check = lambda a, x: x in a

print("Present" if check(a, x) else "Not Present")

"""Q5.WAP TO PRINT FIBONACCI SERIES UP TO N TERMS USING LAMBDA FUNCTION."""
n = int(input("Enter N: "))

fib = lambda a, b: (b, a + b)

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = fib(a, b)

"""Q6.WAP TO PRINT THE INTERSECTION OF 2 ARRAYS USING LAMBDA FUNCTION."""
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

intersection = lambda x, y: list(filter(lambda n: n in y, x))

print("Intersection:", intersection(a, b))
