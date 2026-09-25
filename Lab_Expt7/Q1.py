"""Q1.WAP TO TRIPLE ALL NUMBERS IN A GIVEN LIST OF INTEGERS.USE MAP()"""
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 3, numbers))

print("Original list:", numbers)
print("Tripled list:", result)
