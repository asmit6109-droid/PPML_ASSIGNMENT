"""WAP TO ENTER 2 NUMBER & SWAP THE NUMBER USING BITWISE OPERATION"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)