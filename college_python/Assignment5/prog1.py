def get_unique_elements(input_list):
    """
    Returns a new list containing the unique elements from the input list.
    """
    return list(set(input_list))

# Use a different variable name instead of 'list'
my_list = []

for i in range(6):
    data = int(input("Enter a number: "))
    my_list.append(data)

print("Original List:", my_list)
print("Unique Elements:", get_unique_elements(my_list))
