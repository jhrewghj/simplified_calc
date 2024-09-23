import math

def calculator(expression):
  """
  This function runs a simple calculator that can handle basic arithmetic operations,
  as well as square root, sine, cosine, and tangent.
  """

  # Replace "sqrt" with "math.sqrt"
  expression = expression.replace("sqrt", "math.sqrt")

  # Replace "sin", "cos", "tan" with corresponding math functions
  expression = expression.replace("sin", "math.sin")
  expression = expression.replace("cos", "math.cos")
  expression = expression.replace("tan", "math.tan")
  expression = expression.replace("^", "**")
  expression = expression.replace("pi", "math.pi")
  expression = expression.replace("e", "math.e")

  result = eval(expression)
  return result

import sympy as sp
import re

def extract_coefficients(equation):
  """Extracts the coefficients from a linear equation."""
  match = re.match(r"(-?\d*)x?\s*(\+|\-)?\s*(-?\d*)y\s*=\s*(-?\d*)", equation)
  if match:
    a = int(match.group(1)) if match.group(1) else 0
    b = int(match.group(3)) if match.group(2) == "+" else -int(match.group(3))
    c = int(match.group(4))
    return a, b, c
  else:
    raise ValueError("Invalid equation format")

def solve_linear_equations(eq1, eq2):
  """Solves a system of two linear equations using Cramer's Rule."""

  # Get the equations from the user

  # Extract the coefficients
  a, b, c = extract_coefficients(eq1)
  d, e, f = extract_coefficients(eq2)

  # Calculate determinants
  D = a * e - b * d
  Dx = c * e - b * f
  Dy = a * f - c * d

  # Check for a unique solution
  if D == 0:
    if Dx == 0 and Dy == 0:
      return "Infinite Solutions"
    else:
      return "No Solution"
  else:
    # Calculate and display the solution
    x = Dx / D
    y = Dy / D
    print("\nSolution:")
    print(f"x = {x}")
    print(f"y = {y}")
    return f"x = {x}  y = {y}"
