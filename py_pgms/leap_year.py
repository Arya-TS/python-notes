'''
a leap year or not
'''

year = int(input("Enter year: "))
if year % 400 == 0 or year % 4 == 0:
    print("leap year")
else:
    print("not leap year")
