a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

print("Before swapping:")
print("A =", a)
print("B =", b)

a, b = b, a

print("After swapping:")
print("A =", a)
print("B =", b)