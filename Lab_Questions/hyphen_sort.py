"""Question 11(A)
Accept a hyphen-separated sequence of words, sort them alphabetically,
and print them in a hyphen-separated sequence.
"""

words = input("Enter hyphen-separated words: ")
sorted_words = "-".join(sorted(words.split("-")))
print(sorted_words)
