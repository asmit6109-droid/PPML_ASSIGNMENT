"""Q6.WAP TO PRINT THE INTERSECTION OF 2 ARRAYS USING LAMBDA FUNCTION."""
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

intersection = lambda x, y: list(filter(lambda n: n in y, x))

print("Intersection:", intersection(a, b))