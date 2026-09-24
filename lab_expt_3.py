"""WAP TO PRINT TWIN PRIME NUMBER 1 TO N"""

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input("Enter N: "))

print("Twin prime numbers are:")

for i in range(2, n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)

"""Q2.WAP TO FIND FACTORIALS OF NUM"""

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "is", fact)

"""Q3.WAP TO CHECK LEAP YEAR"""

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

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

"""Q5.WAP TO PRINT EVEN LENGTH WORDS IN A STRING"""

string = input("Enter a string: ")

words = string.split()

print("Even length words are:")

for word in words:
    if len(word) % 2 == 0:
        print(word)

"""Q6.WAP TO REMOVE ALL DUPLICATES FROM A STRING"""

string = input("Enter a string: ")

result = ""

for char in string:
    if char not in result:
        result = result + char

print("String after removing duplicates:", result)
