def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def kth_largest_factor(n, k):
    factors = get_factors(n)
    factors.sort(reverse=True)
    
    if k <= len(factors):
        return factors[k - 1]
    else:
        return None

n = int(input("Enter number N: "))
k = int(input("Enter k (kth largest): "))

result = kth_largest_factor(n, k)
if result:
    print(f"The {k}th largest factor of {n} is: {result}")
else:
    print("Invalid k value!")

# Example
print("\n--- Example ---")
print(f"Factors of 12: {get_factors(12)}")
print(f"3rd largest factor: {kth_largest_factor(12, 3)}")
