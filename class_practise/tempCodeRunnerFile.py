def divide_numbers(a, b):
    try:
        print("Attempting division...")
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    else:
        print(f"Result: {result}")
    finally:
        print("Division attempt complete.")

divide_numbers(10, 2)  # Valid division
divide_numbers(10, 0)  # Division by zero
divide_numbers("10", 2)  # Type error