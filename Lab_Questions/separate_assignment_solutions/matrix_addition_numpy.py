"""Add two matrices using NumPy."""

import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

C = A + B

print("First matrix:")
print(A)
print("\nSecond matrix:")
print(B)
print("\nSum matrix:")
print(C)
