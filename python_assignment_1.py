# ============================================================
# PPML ASSIGNMENT - 1
# ============================================================


# ============================================================
# QUESTION 1: Variables, Assignments & Basic Syntax
#
# Scenario:
# You are building an e-commerce checkout system. A user adds
# an item priced at $19.99 with a quantity of 3. During a
# promotional sale, the store applies a flat discount of $5.00
# before tax and an 8% sales tax afterward.
#
# Task:
# Write a Python script using multiple variable assignment where
# applicable. Read user input for item price and quantity, format
# multi-line log output using triple quotes, and calculate the
# total amount payable rounded to 2 decimal places.
# ============================================================

price, quantity = float(input("Enter item price: ")), int(input("Enter quantity: "))

subtotal = price * quantity
discount = 5.00
tax_rate = 0.08

taxable_amount = subtotal - discount
tax = taxable_amount * tax_rate
total = round(taxable_amount + tax, 2)

print(f"""
E-COMMERCE CHECKOUT
-------------------
Item Price    : ${price:.2f}
Quantity      : {quantity}
Subtotal      : ${subtotal:.2f}
Discount      : ${discount:.2f}
Tax (8%)      : ${tax:.2f}
Total Payable : ${total:.2f}
""")


# ============================================================
# QUESTION 2: Operators & Type Conversion
#
# Scenario:
# A smart security door requires authentication. It checks
# three conditions:
#
# 1. The passcode matches the secret key (Integer comparison).
# 2. The RFID badge ID exists in a predefined list of active IDs
#    (Membership operator).
# 3. The user's role is not "GUEST" (Logical & Identity operator).
#
# Task:
# Prompt the user for a numeric passcode, read their badge ID
# as a string, convert types safely, and output a boolean decision
# (True to unlock, False to deny entry) using logical, membership,
# and bitwise flags for permissions.
# ============================================================

SECRET_KEY = 1234
ACTIVE_IDS = ["RF101", "RF102", "RF103"]

try:
    passcode = int(input("Enter numeric passcode: "))
except ValueError:
    passcode = -1

badge_id = input("Enter RFID badge ID: ").strip()
role = input("Enter role: ").strip().upper()

passcode_match = passcode == SECRET_KEY
badge_active = badge_id in ACTIVE_IDS
role_allowed = role != "GUEST"

# Bitwise permission flags:
# 1 = valid passcode
# 2 = valid badge
# 4 = allowed role
permission_flags = (
    (1 if passcode_match else 0)
    | (2 if badge_active else 0)
    | (4 if role_allowed else 0)
)

unlock = passcode_match and badge_active and role_allowed

print("Passcode Match :", passcode_match)
print("Badge Active   :", badge_active)
print("Role Allowed   :", role_allowed)
print("Permission Flag:", permission_flags)
print("Unlock Decision:", bool(unlock))


# ============================================================
# QUESTION 3: Strings & Built-in Methods
#
# Scenario:
# You are working on a data pipeline that processes unformatted
# log strings:
#
# "USER_ID: 10423 | ACTION: LOGIN | TIMESTAMP: 2026-08-05"
#
# Task:
# Clean the text by stripping whitespace, splitting the fields
# into key-value pairs using string methods (split, strip),
# standardizing actions to lowercase, and formatting a clean
# summary string like:
#
# "User 10423 performed login on 2026-08-05"
# ============================================================

log = " USER_ID: 10423 | ACTION: LOGIN | TIMESTAMP: 2026-08-05 "

fields = log.strip().split("|")
data = {}

for field in fields:
    key, value = field.strip().split(":")
    data[key.strip()] = value.strip()

summary = (
    f"User {data['USER_ID']} performed "
    f"{data['ACTION'].lower()} on {data['TIMESTAMP']}"
)

print(summary)


# ============================================================
# QUESTION 4: Lists & Tuples
#
# Scenario:
# An inventory management system tracks product IDs as immutable
# tuples (product_id, sku, category) and daily stock counts as a
# dynamic list.
#
# Task:
# Create a script that takes a list of daily stock additions,
# removes out-of-stock items (0 values) using list methods,
# sorts the remaining stock in descending order, and binds each
# stock number to its respective immutable product metadata tuple.
# ============================================================

product1 = (101, "SKU101", "Electronics")
product2 = (102, "SKU102", "Books")
product3 = (103, "SKU103", "Clothing")
product4 = (104, "SKU104", "Grocery")

products = [product1, product2, product3, product4]
stock = [25, 0, 15, 40]

# Remove out-of-stock items
while 0 in stock:
    stock.remove(0)

# Sort remaining stock in descending order
stock.sort(reverse=True)

# Bind stock numbers with product metadata
inventory = list(zip(stock, products[:len(stock)]))

for stock_count, product in inventory:
    print(f"Product: {product}, Stock: {stock_count}")


# ============================================================
# QUESTION 5: Sets & Dictionaries
#
# Scenario:
# An online event platform needs to analyze registration data:
#
# Event A attendee emails:
# {"alice@test.com", "bob@test.com", "charlie@test.com"}
#
# Event B attendee emails:
# {"bob@test.com", "david@test.com"}
#
# Task:
# Use set operations to find:
#
# 1. Attendees who attended both events.
# 2. Attendees who attended only one event.
#
# Then, build a dictionary where keys are email addresses and
# values are dictionaries containing profile status
# (e.g., {"is_vip": True}). Clean and access data using
# dictionary methods like .get(), .items(), and .update().
# ============================================================

event_a = {
    "alice@test.com",
    "bob@test.com",
    "charlie@test.com"
}

event_b = {
    "bob@test.com",
    "david@test.com"
}

# Attendees who attended both events
both_events = event_a.intersection(event_b)

# Attendees who attended only one event
only_one_event = event_a.symmetric_difference(event_b)

print("Attended both events:", both_events)
print("Attended only one event:", only_one_event)

# Create profile dictionary
profiles = {
    email: {"is_vip": False}
    for email in event_a.union(event_b)
}

# Update profile
profiles["alice@test.com"].update({"is_vip": True})

# Access dictionary using get() and items()
for email, profile in profiles.items():
    vip_status = profile.get("is_vip", False)
    print(email, "->", profile, "| VIP:", vip_status)


# ============================================================
# QUESTION 6: Control Flow & Loop Manipulation
#
# Scenario:
# An automated ATM system allows users to withdraw cash up to a
# balance of $500. The user can attempt up to 3 PIN entries.
# Once logged in, they enter withdrawal amounts in multiples of 10.
#
# Task:
# Write a program using while loops, if-elif-else branches, and
# loop control keywords (break, continue, pass, else on loops)
# to handle:
#
# - Incorrect PIN retries (max 3).
# - Skipping invalid amounts (not divisible by 10) using continue.
# - Exiting the loop gracefully with a completion message via
#   the else block when cash is successfully disbursed.
# ============================================================

CORRECT_PIN = "1234"
balance = 500
attempts = 0
logged_in = False

# PIN authentication
while attempts < 3:
    pin = input("Enter PIN: ")
    attempts += 1

    if pin == CORRECT_PIN:
        logged_in = True
        print("Login successful.")
        break

    elif attempts < 3:
        print("Incorrect PIN. Try again.")

    else:
        print("Maximum PIN attempts reached.")

# Withdrawal
if logged_in:

    while balance > 0:

        try:
            amount = int(
                input(f"Enter withdrawal amount (Balance ${balance}): ")
            )
        except ValueError:
            print("Invalid input.")
            continue

        if amount <= 0 or amount % 10 != 0:
            print("Invalid amount. Enter a positive multiple of 10.")
            continue

        elif amount > balance:
            print("Insufficient balance.")
            continue

        else:
            pass

        balance -= amount

        print(f"Cash of ${amount} disbursed.")
        break

    else:
        print("ATM transaction completed.")

else:
    print("Access denied.")


# ============================================================
# QUESTION 7: Range Iteration over Collections
#
# Scenario:
# A teacher wants to calculate grade statistics from a list of
# student records represented as dictionaries:
#
# [{"name": "Ana", "score": 85}, {"name": "Ben", "score": 42}]
#
# Task:
# Use a for loop with range() and direct collection iteration
# to process the list. Categorize scores (A for, B for, F for),
# increment pass/fail counters, and construct a summary dict
# mapping names to final letter grades.
# ============================================================

students = [
    {"name": "Ana", "score": 85},
    {"name": "Ben", "score": 42}
]

summary = {}
pass_count = 0
fail_count = 0

# Direct collection iteration
for student in students:

    score = student["score"]

    if score >= 80:
        grade = "A"

    elif score >= 50:
        grade = "B"

    else:
        grade = "F"

    summary[student["name"]] = grade

    if grade == "F":
        fail_count += 1
    else:
        pass_count += 1

# Iteration using range()
for i in range(len(students)):
    print(
        students[i]["name"],
        "->",
        summary[students[i]["name"]]
    )

print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("Summary:", summary)


# ============================================================
# QUESTION 8: Functions, Arguments & Recursion
#
# Scenario:
# A logistics company calculates shipping fees based on distance,
# package weight, and delivery options (standard or express).
# They also need to calculate compound delivery delays over time
# using factorial logic.
#
# Task:
#
# 1. Write a function calculate_shipping(*weights, distance,
#    delivery_type="standard", **surcharges) demonstrating
#    positional, default, *args, and **kwargs.
#
# 2. Write a recursive function calculate_delay_factor(n) that
#    returns to model compound delay points for transit hops.
# ============================================================

def calculate_shipping(
    *weights,
    distance,
    delivery_type="standard",
    **surcharges
):
    base_rate = 2.0
    weight_fee = sum(weights) * 1.5
    distance_fee = distance * 0.10

    if delivery_type.lower() == "express":
        delivery_fee = 20
    else:
        delivery_fee = 0

    extra_fee = sum(surcharges.values())

    total = (
        base_rate
        + weight_fee
        + distance_fee
        + delivery_fee
        + extra_fee
    )

    return round(total, 2)


def calculate_delay_factor(n):
    if n <= 1:
        return 1

    return n * calculate_delay_factor(n - 1)


shipping_fee = calculate_shipping(
    2.5,
    1.5,
    distance=100,
    delivery_type="express",
    fuel_surcharge=5,
    handling_fee=3
)

print("Shipping Fee:", shipping_fee)
print("Delay Factor:", calculate_delay_factor(5))


# ============================================================
# QUESTION 9: Lambda, Map, Filter, and Reduce
#
# Scenario:
# You are analyzing sensor temperature readings in Celsius:
#
# [18.5, 22.0, 31.2, 14.0, 27.8, 35.1]
#
# Task:
#
# 1. Use filter() with a lambda to extract temperatures higher
#    than 20.0°C.
#
# 2. Use map() with a lambda to convert those selected
#    temperatures to Fahrenheit.
#
# 3. Use functools.reduce() to find the sum of all converted
#    Fahrenheit temperatures.
# ============================================================

from functools import reduce

temperatures = [
    18.5,
    22.0,
    31.2,
    14.0,
    27.8,
    35.1
]

# Filter temperatures above 20°C
selected = list(
    filter(lambda c: c > 20.0, temperatures)
)

# Convert Celsius to Fahrenheit
fahrenheit = list(
    map(
        lambda c: round((c * 9 / 5) + 32, 2),
        selected
    )
)

# Find sum using reduce()
total_fahrenheit = reduce(
    lambda x, y: x + y,
    fahrenheit,
    0
)

print("Temperatures above 20°C:", selected)
print("Fahrenheit values:", fahrenheit)
print(
    "Sum of Fahrenheit values:",
    round(total_fahrenheit, 2)
)


# ============================================================
# QUESTION 10: Generators, Decorators & Nested Functions
#
# Scenario:
# You need to monitor performance and memory efficiency for a
# stream of financial transaction logs.
#
# Task:
#
# 1. Create a decorator execution_logger(func) that prints the
#    execution time and function name before and after invocation.
#
# 2. Write a generator function stream_transactions(log_list)
#    using yield that streams transactions one by one instead
#    of loading all into memory at once.
#
# 3. Apply the decorator to a function that processes the
#    generator output.
# ============================================================

import time
from functools import wraps


def execution_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Starting function: {func.__name__}")

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"Finished function: {func.__name__}")

        print(
            f"Execution time: "
            f"{end_time - start_time:.6f} seconds"
        )

        return result

    return wrapper


def stream_transactions(log_list):

    for transaction in log_list:
        yield transaction


@execution_logger
def process_transactions(log_generator):

    total = 0

    for transaction in log_generator:

        print("Processing:", transaction)

        total += transaction["amount"]

    return total


transactions = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": 250},
    {"id": 3, "amount": 750}
]

transaction_stream = stream_transactions(transactions)

total_amount = process_transactions(transaction_stream)

print("Total Transaction Amount:", total_amount)


# ============================================================
# QUESTION 11: Modules & Package Structure
#
# Scenario:
# You are organizing a banking application into a modular Python
# package structure:
#
# bank_app/
# │── __init__.py
# │── accounts/
# │   │── __init__.py
# │   └── savings.py
# └── utils/
#     │── __init__.py
#     └── validators.py
#
# Task:
#
# 1. Define a validation helper function in validators.py.
#
# 2. Import and use that helper inside savings.py using
#    relative/absolute imports.
#
# 3. Write a main execution script outside the package that
#    imports the bank_app package, creates a savings account,
#    and invokes its methods.
#
# ============================================================
#
# NOTE:
# Question 11 requires multiple files because it specifically
# asks for a Python package structure.
#
# Create the following files:
#
# bank_app/
# ├── __init__.py
# ├── accounts/
# │   ├── __init__.py
# │   └── savings.py
# └── utils/
#     ├── __init__.py
#     └── validators.py
#
# main.py
#
#
# ============================================================
# FILE 1: bank_app/utils/validators.py
# ============================================================

# def validate_amount(amount):
#     return isinstance(amount, (int, float)) and amount > 0


# ============================================================
# FILE 2: bank_app/accounts/savings.py
# ============================================================

# from ..utils.validators import validate_amount
#
#
# class SavingsAccount:
#
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def deposit(self, amount):
#
#         if validate_amount(amount):
#             self.balance += amount
#             return f"Deposited ${amount:.2f}"
#
#         return "Invalid deposit amount."
#
#     def withdraw(self, amount):
#
#         if not validate_amount(amount):
#             return "Invalid withdrawal amount."
#
#         if amount > self.balance:
#             return "Insufficient balance."
#
#         self.balance -= amount
#
#         return f"Withdrawn ${amount:.2f}"
#
#     def show_balance(self):
#         return f"Balance: ${self.balance:.2f}"


# ============================================================
# FILE 3: bank_app/accounts/__init__.py
# ============================================================

# from .savings import SavingsAccount


# ============================================================
# FILE 4: bank_app/utils/__init__.py
# ============================================================

# from .validators import validate_amount


# ============================================================
# FILE 5: bank_app/__init__.py
# ============================================================

# from .accounts import SavingsAccount


# ============================================================
# FILE 6: main.py
# ============================================================

# from bank_app import SavingsAccount
#
#
# account = SavingsAccount("Asmit", 1000)
#
# print(account.show_balance())
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.show_balance())


# ============================================================
# END OF PPML ASSIGNMENT - 1
# ============================================================