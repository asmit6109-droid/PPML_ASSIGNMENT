"""WAP TO ENTER A WORD AND CHECK IF ITS PALINDROME OR NOT"""
word = input("Enter a word: ")

reverse = word[::-1]

if word == reverse:
    print("Palindrome Word")
else:
    print("Not a Palindrome Word")