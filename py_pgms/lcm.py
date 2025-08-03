num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
temp1 = num1
temp2 = num2


i = 2
lcm = 1
while temp1 > 1 and temp2 > 1:
    if temp1 % i == 0 or temp2 % i == 0:
        lcm *= i
        if temp1 % i == 0:
            temp1 = temp1 // i
        if temp2 % i == 0:
            temp2 = temp2 // i
    else:
        i += 1
lcm *= temp1*temp2
print(lcm)
