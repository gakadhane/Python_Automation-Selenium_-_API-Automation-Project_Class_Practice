# Write a program to take the 2 user input
# sum, mul, div

# Logic Building
# Step 1
# I/P - num 1, num 2 -> int or flot = don't assume
# O/P - sum - int, sub - int, div - flot

num1 = float(input("Enter your number1"))
num2 = float(input("Enter your number2"))

# num1 = int(num1)
# num2 = int(num2)

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("sum is = ", sum)
print("sub is = ", sub)
print("mul is = ", mul)
print("div is = ", div)

