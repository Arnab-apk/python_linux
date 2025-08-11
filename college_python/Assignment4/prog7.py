# Example lists
list1 = [10, 20, 30, 40, 50]
list2 = [10, 25, 30, 45, 50]

# Check if sizes match
if len(list1) != len(list2):
    print("Lists must be of the same size!")
else:
    index_found = -1
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            index_found = i
            break

    if index_found != -1:
        print(f"Lists differ at index {index_found}: {list1[index_found]} != {list2[index_found]}")
    else:
        print("Lists are identical.")
