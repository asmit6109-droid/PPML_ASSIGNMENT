"""Q4.WAP TO CHECK IF THE STRING SYMMETRICAL OR PALINDROME"""
# Check whether a string is Symmetrical or Palindrome

string = input("Enter a string: ")

# Check Palindrome
if string == string[::-1]:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")

#CHECK SYMMETRICAL
length = len(string)

if length % 2 == 0:
    mid = length // 2
    if string[:mid] == string[mid:]:
        print("The string is Symmetrical")
    else:
        print("The string is not Symmetrical")
else:
    print("The string is not Symmetrical")