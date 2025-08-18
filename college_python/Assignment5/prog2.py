#Write a python program to show the permutation and combination of an inputted List
from itertools import permutations, combinations

# Take input from user
n = int(input("Enter number of elements in the list: "))
my_list = []

for i in range(n):
    data = input(f"Enter element {i+1}: ")
    my_list.append(data)

print("\nOriginal List:", my_list)

# Show permutations
print("\nAll Permutations:")
for p in permutations(my_list):
    print(p)

# Show combinations of different lengths
print("\nAll Combinations:")
for r in range(1, len(my_list) + 1):
    for c in combinations(my_list, r):
        print(c)
