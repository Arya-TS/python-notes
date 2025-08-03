num = int(input("Enter a number: "))
temp = num

sum = 0

while temp > 0:
    digit = temp % 10
    i = 1
    factorial = 1

    while i <= digit:
        factorial *= i
        i += 1

    sum += factorial
    temp = temp//10

if sum == num:
    print("Strong")
else:
    print("Not strong")
