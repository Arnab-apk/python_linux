"""3. Simple Interest - Calculate using formula SI = (P * R * T) / 100"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (% per annum): "))
time = float(input("Enter time period (in years): "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"\nPrincipal = {principal}")
print(f"Rate = {rate}% p.a.")
print(f"Time = {time} years")
print(f"Simple Interest = {simple_interest}")
print(f"Total Amount = {total_amount}")
