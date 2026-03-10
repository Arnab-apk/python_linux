"""6. Armstrong Number - Check if a number is Armstrong number"""

num = int(input("Enter a number: "))

# An Armstrong number (narcissistic number) is a number that is equal 
# to the sum of its own digits each raised to the power of the number of digits

digits = str(num)
num_digits = len(digits)
sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

if sum_of_powers == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
