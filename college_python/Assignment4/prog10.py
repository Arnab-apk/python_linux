import math

# Example list
data = [10, 20, 30, 40, 50]

# Number of elements
n = len(data)

# Calculate mean
mean = sum(data) / n

# Calculate variance
variance = sum((x - mean) ** 2 for x in data) / n

# Calculate standard deviation
std_dev = math.sqrt(variance)

# Display results
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {round(std_dev,2)}")
