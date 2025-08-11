# Example list of strings
str_list = []



# Assume list has at least one element (given in precondition)
max_length = 0
if len(str_list)>0:
    print("enter the elements of the list- ")
    n=int(input("Enter the number of elements in the list to be entered: "))
    for i in range(n):
        word=input()
    str_list.append(word)
    for s in str_list:
        if len(s) > max_length:
            max_length = len(s)

    print("Length of the longest string:", max_length)
else:
    print("The list should contain atleast one element!")

