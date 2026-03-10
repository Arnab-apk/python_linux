"""Find diagonal sum of a 3x3 matrix using NumPy."""

try:
    import numpy as np
except ImportError:
    print("numpy is not installed. Install it using: pip install numpy")
    raise SystemExit(1)

print("Enter a 3x3 matrix row-wise:")
matrix_data = []
for i in range(3):
    row = list(map(float, input(f"Row {i + 1}: ").split()))
    if len(row) != 3:
        print("Each row must contain exactly 3 values")
        raise SystemExit(1)
    matrix_data.append(row)

matrix = np.array(matrix_data)
diagonal_sum = np.trace(matrix)

print("\nMatrix:\n", matrix)
print("Sum of principal diagonal:", diagonal_sum)
