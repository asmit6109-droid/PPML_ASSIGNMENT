def copy_set(s):
    new_set = set()

    for element in s:
        new_set.add(element)

    return new_set


set1 = eval(input("Enter a Set: "))

set2 = copy_set(set1)

print("Original Set:", set1)
print("New Set:", set2)