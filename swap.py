# Input two numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Print original values
print("Before swapping: a =", a, ", b =", b)

# Swap using tuple unpacking
a, b = b, a

# Print swapped values
print("After swapping: a =", a, ", b =", b)
