"""Q6.WAP TO FIND THE RATIO OF POSITIVE NUMBERS NEGATIVE NUMBERS AND ZEROS IN AN ARRAY"""
numbers = [10, -5, 0, 20, -10, 0, 15, -2, 5]

positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

total = len(numbers)

print("Ratio of positive numbers:", positive / total)
print("Ratio of negative numbers:", negative / total)
print("Ratio of zeros:", zero / total)