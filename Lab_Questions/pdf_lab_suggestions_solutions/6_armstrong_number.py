"""6. Armstrong Number - Check if a number is Armstrong number"""

num = 153

# An Armstrong number is equal to sum of its digits each raised to power of digit count
digits_str = str(num)
num_digits = len(digits_str)
sum_of_powers = sum(int(digit) ** num_digits for digit in digits_str)

print(f"Checking {num}:")
print(f"Number of digits: {num_digits}")
print(f"Calculation: {' + '.join([f'{d}^{num_digits}' for d in digits_str])} = {sum_of_powers}")

if sum_of_powers == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
