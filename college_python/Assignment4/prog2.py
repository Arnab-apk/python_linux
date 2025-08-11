# Input lists
L = [3, 1, 4]
M = [1, 5, 9]

# Make sure both lists have the same length
if len(L) != len(M):
    print("Error: Lists must be of the same size.")
else:
    N = []
    for i in range(len(L)):
        N.append(L[i] + M[i])

    print("Resulting list:", N)
