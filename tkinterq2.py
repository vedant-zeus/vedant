import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the expression sin(x)/cos(x)
expression = sp.sin(x) / sp.cos(x)

# Simplify the expression
simplified_expression = sp.simplify(expression)

# Print the result
print(f"The simplified form of sin(x)/cos(x) is: {simplified_expression}")