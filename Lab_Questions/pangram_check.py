"""Question 14(B)
Check whether a string is a pangram. Return False if the string contains
any non-alphabetic character (excluding spaces).
"""


def is_pangram(s):
    for ch in s:
        if not ch.isalpha() and ch != " ":
            return False
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(s.lower()))


text = input("Enter a string: ")
print(is_pangram(text))
