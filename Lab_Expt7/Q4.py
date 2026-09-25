
"""Q4.WAP TO CONVERT ALL THESE CHARACTERS INTO UPPERCASE AND LOWERCASE AND ELIMINATE DUPLICATE LETTERS FROM A GIVEN SEQUENCE.USE MAP() FUNCTION."""
sequence = "PythonProgramming"

unique = list(dict.fromkeys(sequence))

uppercase = list(map(str.upper, unique))
lowercase = list(map(str.lower, unique))

print("Original sequence:", sequence)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)