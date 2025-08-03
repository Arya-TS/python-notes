string1 = input("Enter a string: ")
i = 0
total_even = 0
total_odd = 0

while i < len(string1):
    if string1[i].isdigit():
        if int(string1[i]) % 2 == 0:
            total_even += 1
        else:
            total_odd += 1
    i += 1

print(
    f"Total number of even digits = {total_even} \n Total number of odd digits = {total_odd}")
