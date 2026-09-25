
"""Q5.WAP TO CONVERT A GIVEN LIST OF INTEGER AND A TUPLE OF INTEGER IN A LIST OF STRING USING MAP()"""
list1 = [1, 2, 3, 4, 5]
tuple1 = (6, 7, 8, 9, 10)

list_result = list(map(str, list1))
tuple_result = list(map(str, tuple1))

print("List of strings:", list_result)
print("Tuple converted to list of strings:", tuple_result)