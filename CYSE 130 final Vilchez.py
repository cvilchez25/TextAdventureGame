#final project: Carolina Vilchez

print("Welcome to Escape the Facility!")

while True:
    print("\nWhat do you want to do?")
    print("1. Find Keycard")
    print("2. Hack System")
    print("3. Help Scientist")
    print("4. Quit")

    choice = input("Enter choice: ")

#3 story paths
    if choice == "1":
        print("You chose the keycard path.")
    elif choice == "2":
        print("You chose the hack path.")
    elif choice == "3":
        print("You chose the scientist path.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")