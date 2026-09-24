"""WAP TO ENTER TIME IN MINUTES AND PRINT IT IN HOURS & MINUTE FORMAT"""
minutes = int(input("Enter time in minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Time =", hours, "hours", remaining_minutes, "minutes")