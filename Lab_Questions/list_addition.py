"""Question 22(B)
Take two lists L and M of the same size, add corresponding elements to form list N.
Example: L=[3,1,4], M=[1,5,9], N=[4,6,13]
"""

L = list(map(int, input("Enter list L elements separated by space: ").split()))
M = list(map(int, input("Enter list M elements separated by space: ").split()))

if len(L) != len(M):
    print("Lists must be of the same size")
else:
    N = [L[i] + M[i] for i in range(len(L))]
    print(f"L = {L}")
    print(f"M = {M}")
    print(f"N = {N}")
