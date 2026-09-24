"""Q6.WAP TO REMOVE ALL DUPLICATES FROM A STRING"""

string = input("Enter a string: ")

result = ""

for char in string:
    if char not in result:
        result = result + char

print("String after removing duplicates:", result)