def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

str=input("Enter a string: ")
u, l = count_case(str)
print(f"Uppercase: {u}, Lowercase: {l}")