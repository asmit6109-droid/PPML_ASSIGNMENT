s = str(input("Enter a string: "))
print("Given string is:", s)
s = list(s)
left = 0
right = len(s) - 1
while left < right:
    s[left],s[right] = s[right],s[left]
    left += 1
    right -= 1
print("Reversed string is:", ''.join(s))