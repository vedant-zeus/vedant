import sympy as sp

# Define the variables
x, y = sp.symbols('x y')

# Define the equations
equation1 = sp.Eq(x + y, 2)
equation2 = sp.Eq(2*x + y, 0)

# Solve the system of equations
solution = sp.solve((equation1, equation2), (x, y))

# Print the result
print(f"The solution of the system of equations is: x = {solution[x]}, y = {solution[y]}")