string1 = input("Enter a string: ")

''''''

for i in range(len(string1)//2):
    if string1[i] != string1[len(string1)-i-1]:
        print("Not")
        break

else:
    print("Pal")
''''''

'''new = ''
for i in string1:
    # i = 'p' -> new = 'p' +'' , i = 'y' -> new = 'y' + 'p', i = 't' -> new = 't' + 'yp' ...
    new = i + new

if string1 == new:
    print("Pal")

else:
    print("Not")'''
