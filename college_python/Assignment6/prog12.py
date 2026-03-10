def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def main():
    string = input("Enter string: ")
    
    if is_palindrome(string):
        print(f"'{string}' is a palindrome")
    else:
        print(f"'{string}' is not a palindrome")

# Test cases
test_strings = ["racecar", "hello", "A man a plan a canal Panama", "12321", "abc"]

print("=== Palindrome Check ===")
for test in test_strings:
    result = is_palindrome(test)
    print(f"'{test}' -> {result}")

print("\n=== Interactive Mode ===")
main()
