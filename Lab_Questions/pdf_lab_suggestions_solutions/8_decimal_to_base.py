"""8. Decimal to Any Base Conversion"""

num = int(input("Enter a decimal number: "))
base = int(input("Enter target base (2-36): "))

if base < 2 or base > 36:
    print("Base should be between 2 and 36")
else:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    if num == 0:
        result = "0"
    else:
        while num > 0:
            result = digits[num % base] + result
            num //= base
    
    base_names = {
        2: "Binary",
        8: "Octal",
        10: "Decimal",
        16: "Hexadecimal"
    }
    
    base_name = base_names.get(base, f"Base {base}")
    print(f"{base_name}: {result}")
