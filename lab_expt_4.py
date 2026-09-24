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

"""Q2.WAP TO CREATE TWO LISTS FIRST LIST CONTAINING 5 STRINGS PRINT BOTH THE LISTS ONE ELEMENT FROM EACH LIST COMBINED AT A TIME"""

list1 = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
list2 = ["Red", "Yellow", "Green", "Blue", "Purple"]

for i in range(5):
    print(list1[i], list2[i])

"""Q3.WAP TO CREATE AN INTEGER LIST OF 20 ELEMENTS INCREASE THE ODD VALUED ELEMENTS BY 5"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] = numbers[i] + 5

print("Updated list:", numbers)

"""Q4.WAP TO CREATE A FUNCTION THAT PRINTS THE FIRST 15 TERMS OF THE FIBONACCI SERIES WITHOUT USING RECURSION"""

def fibonacci():
    a = 0
    b = 1

    for i in range(15):
        print(a, end=" ")
        a, b = b, a + b

fibonacci()

"""Q5.WAP TO CREATE A FUNCTION THAT TAKES LIST AS ARGUEMENT AND RETURNS THE EVEN VALUES OF THE LIST.PRINT THE NEW LIST WITH EVEN VALUES."""

def even_values(numbers):
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    return even


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = even_values(numbers)

print("Original list:", numbers)
print("New list with even values:", new_list)

"""Q6.WAP TO CALCULATE FACTORIAL OF A NUMBER USING RECURSION"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = 5

print("Factorial of", num, "is", factorial(num))
