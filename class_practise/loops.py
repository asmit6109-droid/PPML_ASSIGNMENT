# QUESTION 4
for i in range(1,21,2):
    print(i)

for i in range(1,11):
    print(i * 57)

for j in range(1,51):
    if j==15:
        continue
    if j%3==0:
        print(j)

a = float(input("Enter first number: "))
b= float(input("Enter second number: "))
for k in range(1,1000):
    if k%a==0 and k%b==0:
        print(k)