"""1.WAP TO INPUT TWO DICTIONARIES AND PRINT THE VALUES BY MERGING TWO DICTIONARY"""
def merge_dict(d1,d2):
    d1.update(d2)
    return d1
dict1 = eval(input("Enter First Dictionary:"))
dict2 = eval(input("Enter Second Dictionary:"))

result = merge_dict(dict1,dict2)
print("Values of merged dictionary:",result.values())

"""2.WAP TO CREATE A DICTIONARY AND REMOVE THE DUPLICATE VALUE INSIDE THE DICTINARY"""
def remove_duplicate(d):
    result = {}
    
    for key, value in d.items():
        if value not in result.values():
            result[key] = value
            
    return result


dict1 = eval(input("Enter Dictionary: "))

result = remove_duplicate(dict1)

print("Dictionary after removing duplicate values:", result)

"""3.WAP TO ENTER A DICTIONARY AND REMOVE THE DUPLICATE VALUE INSIDE THE DICTIONARY"""
def remove_duplicate(d):
    result = {}

    for key, value in d.items():
        if value not in result.values():
            result[key] = value

    return result


dict1 = eval(input("Enter Dictionary: "))

result = remove_duplicate(dict1)

print("Dictionary after removing duplicate values:", result)

"""4.WAP TO ENTER A SET AND COPY THE CONTENT OF THE SET INTO A NEW SET ONE ELEMENT AT A TIME"""
def copy_set(s):
    new_set = set()

    for element in s:
        new_set.add(element)

    return new_set


set1 = eval(input("Enter a Set: "))

set2 = copy_set(set1)

print("Original Set:", set1)
print("New Set:", set2)

"""5.WAP TO ENTER TWO SETS AND PERFORM ALL THE SET OPERATIONS ON IT"""
def set_operations(s1, s2):
    print("Union:", s1.union(s2))
    print("Intersection:", s1.intersection(s2))
    print("Difference (S1 - S2):", s1.difference(s2))
    print("Difference (S2 - S1):", s2.difference(s1))
    print("Symmetric Difference:", s1.symmetric_difference(s2))


set1 = eval(input("Enter First Set: "))
set2 = eval(input("Enter Second Set: "))

set_operations(set1, set2)

"""6.WAP TO ENTER TWO DIFFERENT SETS WITH STRING ELEMNTS COMBINE BOTH THE SETS REMOVE ANY DUPLICATES R PRESENT,PRINT NEW SET"""
def combine_sets(s1, s2):
    new_set = s1.union(s2)
    return new_set


set1 = eval(input("Enter First Set: "))
set2 = eval(input("Enter Second Set: "))

result = combine_sets(set1, set2)

print("New Set after combining:", result)
