from new_math import NewMath

nm = NewMath()

print("🧪 NewMath Sample Calculations")
print("----------------------------------")

# Division examples
print("10 / 0 =", nm.divide(10, 0))        # infinity
print("0 / 0 =", nm.divide(0, 0))          # "Undefined"
print("∞ / 5 =", nm.divide(nm.infinity, 5))  # infinity
print("5 / ∞ =", nm.divide(5, nm.infinity))  # 0

# Addition
print("5 + ∞ =", nm.add(5, nm.infinity))     # infinity

# Subtraction
print("∞ - ∞ =", nm.subtract(nm.infinity, nm.infinity))  # "Undefined"
print("∞ - 10 =", nm.subtract(nm.infinity, 10))          # infinity

# Multiplication
print("0 * ∞ =", nm.multiply(0, nm.infinity))            # 0
print("3 * ∞ =", nm.multiply(3, nm.infinity))            # infinity

# Exponentiation
print("∞ ^ 0 =", nm.exponentiate(nm.infinity, 0))        # 1
print("0.5 ^ ∞ =", nm.exponentiate(0.5, nm.infinity))    # 0
print("2 ^ ∞ =", nm.exponentiate(2, nm.infinity))        # infinity

# Equation solving
print("Solve '10 / 0 + 5':", nm.solve_equation("10 / 0 + 5"))  # infinity