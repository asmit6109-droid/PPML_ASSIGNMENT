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