"""1.WAP TO INPUT TWO DICTIONARIES AND PRINT THE VALUES BY MERGING TWO DICTIONARY"""
def merge_dict(d1,d2):
    d1.update(d2)
    return d1
dict1 = eval(input("Enter First Dictionary:"))
dict2 = eval(input("Enter Second Dictionary:"))

result = merge_dict(dict1,dict2)
print("Values of merged dictionary:",result.values())