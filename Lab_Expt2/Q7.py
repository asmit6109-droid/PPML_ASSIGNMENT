"""WAP TO ENTER 3 DIGIT NUMBER AND PRINT ALL THE PRIME FACTORS OF THE NUMBER"""
num = int(input("Enter a 3 digit number: "))

print("Prime factors are:")

i = 2
while num > 1:
    if num % i == 0:
        print(i, end=" ")
        num = num // i
    else:
        i += 1