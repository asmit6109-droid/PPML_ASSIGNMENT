
"""Q3.WAP TO CREATE AN INTEGER LIST OF 20 ELEMENTS INCREASE THE ODD VALUED ELEMENTS BY 5"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] = numbers[i] + 5

print("Updated list:", numbers)