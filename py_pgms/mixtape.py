mixtape = ['🎹 numb', '🎸 fake love', '🎻 shallow']

print("Here's your list of songs: ")
for song in mixtape:
    print(song)

next = 'yes'

while next == 'yes':
    print("What do you want to do next? ")
    print('1) add song \n2) remove song')

    choice = int(input("Enter the choice no: "))

    if choice == 1:
        add = input("Enter the name of the song: ")
        mixtape.append(add)

    elif choice == 2:
        print("Here's your list of songs: ")
        for song in mixtape:
            print(f" - {song}")
        remove = input("Enter the name of the song you want to remove: ")
        if remove in mixtape:
            mixtape.remove(remove)
        else:
            print("No such song in the mixtape!")

    else:
        print("Invalid choice!")

    next = input("Do you want to try again? \nEnter yes/no: ").lower()
    if next == 'no':
        print('See you next time!')

print('Final mixtape: ')
for song in mixtape:
    print(f"- {song}")
