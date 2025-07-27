bucket_list = ['🧹 clean the whole house',
               '💰 sell things not needed anymore', '📚 finish 3 certificate courses']
bucket_list.sort(key=lambda x: x.split(' ', 1)[-1].lower())

print("Here's your bucket list: ")
for item in bucket_list:
    print(f"- {item}")

next_action = 'yes'
while next_action == 'yes':
    print("What do you want to do next? \n1) add 2) remove")
    choice = int(input("Enter the choice number: "))

    if choice == 1:
        add = input("Enter item to add: ")
        bucket_list.append(add)

    elif choice == 2:
        print("Here's your bucket list: ")
        for item in bucket_list:
            print(f"- {item}")
        remove = input("Enter the item to remove: ")
        if remove in bucket_list:
            bucket_list.remove(remove)
        else:
            print("No such item in the list!")
    else:
        print("Invalid choice!")

    print("Do you want to try again? yes/no: ")
    next_action = input().lower()
    if next_action == 'no':
        print("See you next time!")

bucket_list.sort(key=lambda x: x.split(' ', 1)[-1].lower())
print("Final list: ")
for item in bucket_list:
    print(f"- {item}")
print("Total number of items left in the list: ", len(bucket_list))

print("\nKeep dreaming big!")
