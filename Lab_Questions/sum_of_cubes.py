"""Question 21(A)
Input a list of numbers; find those where the number equals the sum of the cubes
of its digits. Print that list along with its smallest and greatest elements.
"""

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result = [n for n in numbers if n == sum(int(d) ** 3 for d in str(abs(n)))]

if result:
    print(f"Numbers equal to sum of cubes of their digits: {result}")
    print(f"Smallest: {min(result)}")
    print(f"Greatest: {max(result)}")
else:
    print("No such numbers found")
