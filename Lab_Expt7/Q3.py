"""Q3.WAP TO CREATE A LIST CONTAINIG THE POWER OF SAID NUMBERS IN BASE RAISED TO THE CORRESPONDING NUMBER IN THE INDEX USING PYTHON MAP"""
numbers = [2, 3, 4, 5]

result = list(map(lambda x, y: x ** y, numbers, range(len(numbers))))

print("Original list:", numbers)
print("Result:", result)