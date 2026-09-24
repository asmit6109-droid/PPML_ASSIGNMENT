"""Q5.WAP TO PRINT EVEN LENGTH WORDS IN A STRING"""

string = input("Enter a string: ")

words = string.split()

print("Even length words are:")

for word in words:
    if len(word) % 2 == 0:
        print(word)