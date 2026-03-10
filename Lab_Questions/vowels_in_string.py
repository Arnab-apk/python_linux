"""Display all vowels in a given string."""

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
found_vowels = [ch for ch in text if ch in vowels]

if found_vowels:
    print("Vowels in the string:", " ".join(found_vowels))
else:
    print("No vowels found in the string")
