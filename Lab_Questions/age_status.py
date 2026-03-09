"""Question 22(A)
Input ages and print status based on standard age-group classification rules.
"""

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age <= 2:
    print("Infant")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")
