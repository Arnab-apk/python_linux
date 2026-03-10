"""Read two matrices and add them using NumPy."""

try:
    import numpy as np
except ImportError:
    print("numpy is not installed. Install it using: pip install numpy")
    raise SystemExit(1)

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter first matrix row-wise:")
mat1 = []
for i in range(rows):
    row = list(map(float, input(f"Row {i + 1}: ").split()))
    if len(row) != cols:
        print("Invalid row length")
        raise SystemExit(1)
    mat1.append(row)

print("Enter second matrix row-wise:")
mat2 = []
for i in range(rows):
    row = list(map(float, input(f"Row {i + 1}: ").split()))
    if len(row) != cols:
        print("Invalid row length")
        raise SystemExit(1)
    mat2.append(row)

A = np.array(mat1)
B = np.array(mat2)
C = A + B

print("\nFirst matrix:\n", A)
print("\nSecond matrix:\n", B)
print("\nSum matrix:\n", C)
