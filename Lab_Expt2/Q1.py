"""WAP TO ENTER a% & DISPLAY THE GRADUATION SYSTEM"""
percentage = float(input("Enter percentage: "))

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
elif percentage >= 40:
    print("Grade: E")
else:
    print("Grade: F")