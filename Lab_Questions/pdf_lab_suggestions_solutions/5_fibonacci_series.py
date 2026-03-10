"""5. Fibonacci Series - Print first n Fibonacci numbers"""

n = 10

if n <= 0:
    print("Number of terms must be positive")
elif n == 1:
    print("Fibonacci series: 0")
else:
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    print(f"Fibonacci series (first {n} terms):")
    print(" ".join(map(str, fib[:n])))
