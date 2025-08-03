string1=input("Enter string: ")
i =0
while i<len(string1):
    if i !=2:
        print(string1[i],end='')
    else:
        print(string1[i].capitalize(),end='')
    i+=1

    