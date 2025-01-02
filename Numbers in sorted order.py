# Enter numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
# Minimum number
a1 = min(x, y, z)
# Maximum number
a3 = max(x, y, z)
# Middle number 
a2 = (x + y + z) - a3 - a1 
# Execute the code 
print(f"Numbers in sorted order {a1}, {a2}, {a3}")

