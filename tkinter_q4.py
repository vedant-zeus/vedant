import numpy as np

# Coefficient matrix A
A = np.array([[3, 7, -1],
              [4, -2, -1]])

# Constant matrix b
b = np.array([12, 5])

# Solve for the variables [x, y, z]
solution = np.linalg.lstsq(A, b, rcond=None)[0]

# Print the result
x, y, z = solution
print(f"The solution is: x = {x}, y = {y}, z = {z}")