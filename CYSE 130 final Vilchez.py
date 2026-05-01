#final project: Carolina Vilchez

# GAME WITH NPC + CHALLENGE
# =========================

import datetime
# GLOBAL VARIABLES
# =========================
inventory = []

# LOGGING FUNCTION
# =========================
def log_event(event):
    with open("audit_log.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - {event}\n")

# SAFE INPUT FUNCTION
# =========================
def safe_input(prompt, valid_choices):
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please try again.")
            log_event("INVALID_INPUT")

# INVENTORY FUNCTIONS
# =========================
def add_item(item):
    if item not in inventory:
        inventory.append(item)
        print(f"You collected: {item}")
        log_event(f"ITEM_ADDED: {item}")

def show_inventory():
    print("\nYour Inventory:")
    if len(inventory) == 0:
        print("Empty")
    else:
        for item in inventory:
            print("-", item)

# NPC + CHALLENGE
# =========================
def guard_encounter():
    print("\nGuard: Stop right there!")
    print("1. Fight")
    print("2. Run")

    choice = safe_input("Choose: ", ["1", "2"])

    if choice == "1":
        print("You defeated the guard and took his key.")
        add_item("Guard Key")
        log_event("GUARD_DEFEATED")
    else:
        print("You escaped safely.")
        log_event("GUARD_ESCAPED")
        

# GAME START
# =========================
print("Welcome to Escape the Facility!")
log_event("GAME_START")

while True:
    print("\nWhat do you want to do?")
    print("1. Find Keycard")
    print("2. Hack System")
    print("3. Help Scientist")
    print("4. View Inventory")
    print("5. Quit")

    choice = safe_input("Enter choice: ", ["1", "2", "3", "4", "5"])

    if choice == "1":
        print("You search the office...")
        guard_encounter()
        add_item("Keycard")
        log_event("CHOICE_KEYCARD")

    elif choice == "2":
        print("You enter the server room.")
        add_item("Hacking Tool")
        log_event("CHOICE_HACK")

    elif choice == "3":
        print("Scientist: Please help me!")
        print("You help the scientist and get a secret code.")
        add_item("Secret Code")
        log_event("CHOICE_SCIENTIST")

    elif choice == "4":
        show_inventory()

    elif choice == "5":
        print("Goodbye!")
        log_event("GAME_END")
        break
