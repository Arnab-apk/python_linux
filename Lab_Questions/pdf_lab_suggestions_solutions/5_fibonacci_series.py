"""5. Fibonacci Series - Print first n Fibonacci numbers"""

n = int(input("Enter number of terms: "))

if n <= 0:
    print("Number of terms must be positive")
elif n == 1:
    print("Fibonacci series:", 0)
else:
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    print("Fibonacci series:")
    for i in range(n):
        print(fib[i], end=" ")
    print()
