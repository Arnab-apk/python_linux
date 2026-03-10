"""Display all vowels in a given string."""

text = "Hello World"
vowels = "aeiouAEIOU"
found_vowels = [ch for ch in text if ch in vowels]

print(f"String: {text}")
print(f"Vowels: {' '.join(found_vowels)}")
