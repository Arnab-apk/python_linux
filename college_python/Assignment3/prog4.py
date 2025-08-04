def is_palindrome(s):
    # Convert to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Take input from user
user_input = input("Enter a string: ")

# Check and print result
if is_palindrome(user_input):
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
