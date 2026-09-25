"""Q5.WAP TO PRINT FIBONACCI SERIES UP TO N TERMS USING LAMBDA FUNCTION."""
n = int(input("Enter N: "))

fib = lambda a, b: (b, a + b)

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = fib(a, b)