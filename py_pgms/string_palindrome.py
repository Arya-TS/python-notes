string1 = input("Enter a string: ")

for i in range(len(string1)//2):
    if string1[i] != string1[len(string1)-i-1]:
        print("Not")
        break

else:
    print("Pal")
