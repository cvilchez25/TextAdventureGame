#final project: Carolina Vilchez

import datetime

# LOGGING FUNCTION
# ========================
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

# GAME START
# =========================

print("Welcome to Escape the Facility!")
log_event("GAME_START")

while True:
    print("\nWhat do you want to do?")
    print("1. Find Keycard")
    print("2. Hack System")
    print("3. Help Scientist")
    print("4. Quit")

    choice = safe_input("Enter choice: ", ["1", "2", "3", "4"])

    if choice == "1":
        print("You chose the keycard path.")
        log_event("CHOICE_KEYCARD")
    elif choice == "2":
        print("You chose the hack path.")
        log_event("CHOICE_HACK")
    elif choice == "3":
        print("You chose the scientist path.")
        log_event("CHOICE_SCIENTIST")
    elif choice == "4":
        print("Goodbye!")
        log_event("GAME_END")
        break
