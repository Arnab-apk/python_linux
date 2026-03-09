"""Question 14(A)
Check whether a number is an Armstrong number or not.
An Armstrong number is one where the sum of its digits each raised to the
power of the number of digits equals the number itself.
"""

num = int(input("Enter a number: ")) #integer 153
digits = str(num)#"153"
n = len(digits)# length 3
total = sum(int(d) ** n for d in digits)

if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

