string1 = input("Enter a string: ")
i = 0
count = 0
total = 0

while i < len(string1):
    if string1[i].isdigit():
        total += int(string1[i])
        count += 1
    i += 1

if count > 0:
    print(f"Average = {total / count}")
else:
    print("No digits found.")
