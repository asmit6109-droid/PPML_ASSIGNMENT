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