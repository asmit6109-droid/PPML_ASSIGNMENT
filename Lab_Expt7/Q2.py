"""Q2.WAP TO ADD THREE GIVEN LIST USING PYTHON MAP AND LAMBDA"""
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]

result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

print("Result:", result)