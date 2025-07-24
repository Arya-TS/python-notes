'''
🎮 Your first text-based game!

💬 Prompt:
You wake up in a mysterious forest… it’s dark, you’re alone, and there are two paths in front of you.
One leads into a creepy cave.
The other leads to a glowing lake.

In this adventure game, the player will navigate through your story by typing choices like "cave" or "lake" in the terminal.

✨ Your job is to write the logic of this choose-your-own-adventure game using input(), if/elif/else, and print statements.

💡 You get to create your own story! Be as weird, funny, spooky, or magical as you want.

Requirements:
Ask the user a starting choice using input()

Use if/elif/else to branch the story based on their choice

Have at least 2 levels of choices (like: go to cave ➤ meet dragon ➤ choose to fight or run)

Print different outcomes based on the path taken

🚨 Bonus Challenge:

Add a twist! Maybe one path leads to treasure, another to a trap! 😱

Add emojis to bring your story to life

🎯 End Goal: Create a simple adventure story that runs in the terminal based on user input.
'''

print("🌲 You wake up in a mysterious forest... surrounded by silence and eternal darkness. As your vision adjusts to the dim moonlight, you see two paths ahead: one leads into a creepy cave, the other to a glowing lake.")

choice1 = input("Which path do you choose? (cave/lake): ").lower()

if choice1 == "cave":
    print("\n🕸️ It's pitch black inside. A shiver runs down your spine as a cool breeze brushes past.")
    choice2 = input(
        "Do you move forward or return? (forward/backward): ").lower()

    if choice2 == "forward":
        print("\n🌟 You hear strange noises, but you keep moving. A silver light appears and grows brighter... Hurray! You made it out! 🥳")
    else:
        print("\n🔁 You return and head toward the glowing lake.")
        print("💧 The moonlight dances on the waves. You spot a box across the lake — it’s a fairy-like lamp with a string and a note: 'Spin me!'")
        print("✨ You spin the lamp... and it lights up! 💡")
        choice3 = input(
            "Do you head back to the cave or wander around? (cave/wander): ").lower()

        if choice3 == "cave":
            print("\n🔦 The lamp lights your path. Inside the cave is peaceful now. You find an exit and rush outside. Hurray! You made it! 🥳")
        else:
            print("\n🌌 You wander into the woods and get lost forever. The End 😳")

elif choice1 == "lake":
    print("\n💧 The moonlight dances on the waves. You spot a box across the lake — it’s a fairy-like lamp with a string and a note: 'Spin me!'")
    print("✨ You spin the lamp... and it lights up! 💡")
    choice4 = input(
        "Do you head back to the cave or wander around? (cave/wander): ").lower()

    if choice4 == "cave":
        print("\n🔦 The lamp lights your path. Inside the cave is peaceful now. You find an exit and rush outside. Hurray! You made it! 🥳")
    else:
        print("\n🌌 You wander into the woods and get lost forever. The End 😳")

else:
    print("\n😕 You hesitate for too long and wander aimlessly... and get lost in the forest. The End.")
