num = int(input("Enter the number"))
order = len(str(num))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == num:
    print("This is the armstrong number")
else:
    print("This is not the armstrong number")
