import string

def is_pangram(s):
    s = s.lower()
    return set(string.ascii_lowercase).issubset(set(s))

str=input("Enter a string: ")
print(is_pangram(str))
