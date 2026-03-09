"""Question 13(A)
Find the mean and median of a set of elements.
"""

numbers = list(map(float, input("Enter numbers separated by space: ").split()))

mean = sum(numbers) / len(numbers)

sorted_nums = sorted(numbers)
n = len(sorted_nums)
if n % 2 == 0:
    median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
else:
    median = sorted_nums[n // 2]

print(f"Mean: {mean}")
print(f"Median: {median}")
