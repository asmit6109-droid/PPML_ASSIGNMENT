price = float(input("Enter the price of the item:"))
quantity = int(input("Enter the quantity of the item:"))
total = price * quantity

discounted_price = total - 5
tax = discounted_price * 0.08
final_price = discounted_price + tax

last_price = round(final_price, 2)
print(last_price)

print(f"""
item price: {price}
quantity: {quantity}
total: {total}
discounted price: {discounted_price}
tax: {tax}
final price: {final_price}
last price: {last_price}
""")
