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