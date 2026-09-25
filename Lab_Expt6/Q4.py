"""Q4.WAP TO CHECK IF A VALUE IS PRESENT IN THE LIST OR NOT,USING LAMBDA FUNCTION."""
a = list(map(int, input("Enter list: ").split()))
x = int(input("Enter value: "))

check = lambda a, x: x in a

print("Present" if check(a, x) else "Not Present")
