def set_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    
    return True

#ASSERT
def apply_discount(price,discount_rate):
    assert 0 <= discount_rate <= 1, "Discount rate must be between 0 and 1."
    return price - (price * discount_rate)
final_price = apply_discount(100, 0.2)
print(final_price)

#
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

