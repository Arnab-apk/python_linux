# Create the list
result = []

for i in range(26):
    letter = chr(97 + i)     # 97 is ASCII code for 'a'
    result.append(letter * (i + 1))

print(result)
