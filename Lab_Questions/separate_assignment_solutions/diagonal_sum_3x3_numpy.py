"""Find diagonal sum of a 3x3 matrix using NumPy."""

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

diagonal_sum = np.trace(matrix)

print("Matrix:")
print(matrix)
print(f"\nSum of principal diagonal: {diagonal_sum}")
