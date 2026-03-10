def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    return [n for n in range(2, limit) if is_prime(n)]

def prime_sum(limit):
    primes = get_primes(limit)
    
    for prime in primes:
        for i in range(len(primes)):
            current_sum = 0
            temp = []
            for j in range(i, len(primes)):
                current_sum += primes[j]
                temp.append(primes[j])
                if current_sum == prime and len(temp) > 1:
                    print(f"{prime} = {' + '.join(map(str, temp))}")
                    break
                if current_sum > prime:
                    break

prime_sum(30)
