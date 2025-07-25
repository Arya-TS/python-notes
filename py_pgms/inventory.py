items = ['🪛  screw', '🔨 hammer', '🔪 knife', '✂️  scissors']
print("Here's a list of your items in the inventory:")
for item in items:
    print(f"- {item}")

print("\nChoose from:")
print("1) Append")
print("2) Remove")

choice = int(input("Enter the choice number: "))

if choice == 1:
    add = input("Enter item to add: ")
    items.append(add)

elif choice == 2:
    remove = input("Enter the item to remove: ")
    if remove in items:
        items.remove(remove)
    else:
        print("No such item in the inventory!")

print("Your current list of items: ")
for item in items:
    print(f"- {item}")
