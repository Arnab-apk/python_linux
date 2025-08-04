def reduce_string_recursive(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            # Remove the pair and call the function again
            return reduce_string_recursive(s[:i] + s[i+2:])
        i += 1
    return s

# Examples
str=input("Enter a sting: ")
print(f"The reduced string is : {reduce_string_recursive(str)}")# Output: ""

