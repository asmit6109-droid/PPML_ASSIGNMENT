
"""Q4.WAP TO CREATE A FUNCTION THAT PRINTS THE FIRST 15 TERMS OF THE FIBONACCI SERIES WITHOUT USING RECURSION"""

def fibonacci():
    a = 0
    b = 1

    for i in range(15):
        print(a, end=" ")
        a, b = b, a + b

fibonacci()