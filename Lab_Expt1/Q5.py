"""WAP TO ENTER A TEMPERATURE IN FAREINHEIT & CONVERT TO CELCIUS"""
f = float(input("Enter temperature in Fahrenheit: "))

c = (f - 32) * 5 / 9

print("Temperature in Celsius =", c)