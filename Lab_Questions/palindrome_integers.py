"""Question 20(B)
Given a list of integers, find those which are palindromes.
"""

numbers = list(map(int, input("Enter integers separated by space: ").split()))
palindromes = [n for n in numbers if str(abs(n)) == str(abs(n))[::-1]]
print(f"Palindromes: {palindromes}")
