"""WAP TO ENTER A STRING AND PRINT IT IN REVERSE ALSO PRINT THE NO. OF VOWELS AND CONSONANT IN IT"""
string = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in string:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Reverse of string =", string[::-1])
print("Number of vowels =", vowels)
print("Number of consonants =", consonants)