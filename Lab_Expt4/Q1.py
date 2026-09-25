"""Q1.WAP TO PRINT SECOND LARGEST AND SECOND SMALLEST ELEMENT IN A LIST OF 10 INTEGERS WITHOUT USING SORT()"""

numbers = [10, 25, 5, 40, 15, 30, 20, 8, 35, 12]

largest = second_largest = float('-inf')
smallest = second_smallest = float('inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second largest:", second_largest)
print("Second smallest:", second_smallest)