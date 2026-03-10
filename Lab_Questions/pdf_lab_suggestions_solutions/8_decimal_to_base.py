"""8. Decimal to Any Base Conversion"""

num = 255
bases = [2, 8, 16]

print(f"Converting {num} to different bases:\n")

for base in bases:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    temp = num
    
    if temp == 0:
        result = "0"
    else:
        while temp > 0:
            result = digits[temp % base] + result
            temp //= base
    
    base_names = {2: "Binary", 8: "Octal", 16: "Hexadecimal"}
    base_name = base_names.get(base, f"Base {base}")
    print(f"{base_name}: {result}")
