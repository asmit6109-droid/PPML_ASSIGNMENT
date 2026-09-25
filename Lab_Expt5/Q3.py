"""3.WAP TO CREATE A DICTIONARY AND PRINT THE KEY WHICH HAS THE MAXIMUM UNIQUE VALUE"""
def maximum_unique_value(d):
    max_value = None
    max_key = None

    for key, value in d.items():
        if list(d.values()).count(value) == 1:
            if max_value is None or value > max_value:
                max_value = value
                max_key = key

    return max_key


dict1 = eval(input("Enter Dictionary: "))

result = maximum_unique_value(dict1)

print("Key having maximum unique value:", result)