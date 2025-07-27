'''list = []
items = input("Enter items sepaarted by comma(,): ")
list.extend(item.strip() for item in items.split(','))
print(list)'''

# another method

my_list = []
print("Enter the items (type done to finish): ")
while True:
    items = input().strip()
    if items.lower() == 'done':
        break
    my_list.append(items)

print("Your final list:")
print(my_list)
