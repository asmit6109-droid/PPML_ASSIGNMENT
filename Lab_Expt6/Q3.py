"""Q3.WAP TO PRINT THE TRANSPOSE OF A MATRIX OF N*N ORDER"""
def transpose(a):
    for j in range(n):
        print([a[i][j] for i in range(n)])

n = int(input("Enter N: "))
a = [list(map(int, input().split())) for i in range(n)]

print("Transpose:")
transpose(a)