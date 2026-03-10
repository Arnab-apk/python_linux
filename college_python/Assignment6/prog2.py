def get_consecutive_integers(start=1):
    return list(range(start, start + 10))

result = get_consecutive_integers(1)
print("Ten consecutive integers:", result)

# Custom start
result2 = get_consecutive_integers(5)
print("Ten consecutive integers starting from 5:", result2)
