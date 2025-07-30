compnum = 50
count = 1
num = int(input("Enter a number: "))
while num != compnum:
    if num < compnum:
        print("Your guess is too low")
        num = int(input("Have another guess: "))
        count += 1
    else:
        print("Your guess is too high")
        num = int(input("Have another guess: "))
        count += 1

print(f"Well done, you took {count} attempts")
