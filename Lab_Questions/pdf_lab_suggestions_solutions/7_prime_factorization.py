"""7. Prime Factorization - Find all prime factors of a number"""

num = 60

if num <= 1:
    print("Number must be greater than 1")
else:
    prime_factors = []
    temp = num
    
    # Check for factor 2
    while temp % 2 == 0:
        prime_factors.append(2)
        temp //= 2
    
    # Check for odd factors from 3 onwards
    i = 3
    while i * i <= temp:
        while temp % i == 0:
            prime_factors.append(i)
            temp //= i
        i += 2
    
    # If temp is still > 1, it's a prime factor
    if temp > 1:
        prime_factors.append(temp)
    
    print(f"Prime factors of {num}: {prime_factors}")
    print(f"Factorization: {' × '.join(map(str, prime_factors))}")
