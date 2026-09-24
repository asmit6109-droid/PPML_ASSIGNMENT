a = float(input("Enter num1:"))
b = float(input("Enter num2:"))
c = input("Enter operator:")

if c == '+':
    print(a+b)
elif c =='-':
    print(a-b)
elif c== '*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='%':
    print(a%b)
elif c=='**':
    print(a**b)
else:
    print("Invalid operator")