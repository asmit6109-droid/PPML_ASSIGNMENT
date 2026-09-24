"""Q1.WAP TO TRIPLE ALL NUMBERS IN A GIVEN LIST OF INTEGERS.USE MAP()"""
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 3, numbers))

print("Original list:", numbers)
print("Tripled list:", result)

"""Q2.WAP TO ADD THREE GIVEN LIST USING PYTHON MAP AND LAMBDA"""
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]

result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

print("Result:", result)

"""Q3.WAP TO CREATE A LIST CONTAINIG THE POWER OF SAID NUMBERS IN BASE RAISED TO THE CORRESPONDING NUMBER IN THE INDEX USING PYTHON MAP"""
numbers = [2, 3, 4, 5]

result = list(map(lambda x, y: x ** y, numbers, range(len(numbers))))

print("Original list:", numbers)
print("Result:", result)

"""Q4.WAP TO CONVERT ALL THESE CHARACTERS INTO UPPERCASE AND LOWERCASE AND ELIMINATE DUPLICATE LETTERS FROM A GIVEN SEQUENCE.USE MAP() FUNCTION."""
sequence = "PythonProgramming"

unique = list(dict.fromkeys(sequence))

uppercase = list(map(str.upper, unique))
lowercase = list(map(str.lower, unique))

print("Original sequence:", sequence)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

"""Q5.WAP TO CONVERT A GIVEN LIST OF INTEGER AND A TUPLE OF INTEGER IN A LIST OF STRING USING MAP()"""
list1 = [1, 2, 3, 4, 5]
tuple1 = (6, 7, 8, 9, 10)

list_result = list(map(str, list1))
tuple_result = list(map(str, tuple1))

print("List of strings:", list_result)
print("Tuple converted to list of strings:", tuple_result)

"""Q6.WAP TO FIND THE RATIO OF POSITIVE NUMBERS NEGATIVE NUMBERS AND ZEROS IN AN ARRAY"""
numbers = [10, -5, 0, 20, -10, 0, 15, -2, 5]

positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

total = len(numbers)

print("Ratio of positive numbers:", positive / total)
print("Ratio of negative numbers:", negative / total)
print("Ratio of zeros:", zero / total)
