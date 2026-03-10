def format_number(num):
    return f"{num:,}"

# Test cases
test_numbers = [1000, 1000000, 12345, 999, 1234567]

for num in test_numbers:
    print(f"{num} -> {format_number(num)}")
