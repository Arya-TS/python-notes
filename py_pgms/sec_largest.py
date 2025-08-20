# Find the second largest number in a list
num = [1, 7, 3, 4, 2, 0, 5, -1]

largest = num[0]
sec_largest = num[1]

for i in num:
    if i > largest:
        sec_largest = largest
        largest = i

    elif i < largest and i > sec_largest:
        sec_largest = i

print(sec_largest)
