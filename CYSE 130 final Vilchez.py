#final project: Carolina Vilchez


# FINAL GAME VERSION
# =========================
import datetime
inventory = []

# LOGGING
# =========================
def log_event(event):
    with open("audit_log.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - {event}\n")

# SAFE INPUT
# =========================
def safe_input(prompt, valid_choices):
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice, Try again.")
            log_event("INVALID_INPUT")

# INVENTORY
# =========================
def add_item(item):
    if item not in inventory:
        inventory.append(item)
        print(f"You got: {item}")
        log_event(f"ITEM_ADDED: {item}")

def show_inventory():
    print("\nInventory:")
    if not inventory:
        print("Empty")
    else:
        for item in inventory:
            print("-", item)

# NPCS
# =========================
def guard():
    print("\nGuard: You can't pass!")
    print("1. Fight")
    print("2. Run")

    choice = safe_input("Choose: ", ["1", "2"])

    if choice == "1":
        print("You beat the guard")
        add_item("Guard Key")
        log_event("GUARD_FIGHT")
    else:
        print("You ran away")
        log_event("GUARD_RUN")

def scientist():
    print("\nScientist: Help me!")
    print("You help the scientist")
    add_item("Secret Code")
    log_event("SCIENTIST_HELP")

def hacker():
    print("\nHacker: I'll help you")
    add_item("Hacking Tool")
    log_event("HACKER_HELP")

def medic():
    print("\nMedic gives you a med kit")
    add_item("Med Kit")
    log_event("MEDIC_HELP")

def robot():
    print("\nRobot gives access chip")
    add_item("Access Chip")
    log_event("ROBOT_HELP")

# CHALLENGE 2
# =========================
def password_puzzle():
    print("\nTerminal locked (hint: 2026)")
    attempt = input("Enter password: ")

    if attempt == "2026":
        print("Access granted")
        log_event("PASSWORD_SUCCESS")
        return True
    else:
        print("Wrong password")
        log_event("PASSWORD_FAIL")
        return False

# PATHS
# =========================
def path_keycard():
    print("\nYou go find a keycard")
    guard()
    medic()

    if "Guard Key" in inventory:
        print("You unlocked the door and escaped!")
        log_event("ENDING_KEYCARD")
    else:
        print("You couldn't escape")
        log_event("ENDING_FAIL")

def path_hack():
    print("\nYou try hacking")
    hacker()
    robot()

    if password_puzzle():
        print("You hacked the system and escaped!")
        log_event("ENDING_HACK")
    else:
        print("Hack failed")
        log_event("ENDING_FAIL")

def path_scientist():
    print("\nYou follow the scientist")
    scientist()

    if "Secret Code" in inventory:
        print("You found a secret exit and escaped!")
        log_event("ENDING_SECRET")
    else:
        print("You got stuck")
        log_event("ENDING_FAIL")

# MAIN GAME
# =========================
print("Welcome to Escape the Facility!")
log_event("GAME_START")

while True:
    print("\n1. Find Keycard")
    print("2. Hack System")
    print("3. Help Scientist")
    print("4. Inventory")
    print("5. Quit")

    choice = safe_input("Choose: ", ["1","2","3","4","5"])

    if choice == "1":
        path_keycard()
    elif choice == "2":
        path_hack()
    elif choice == "3":
        path_scientist()
    elif choice == "4":
        show_inventory()
    elif choice == "5":
        print("Bye.")
        log_event("GAME_END")
        break
