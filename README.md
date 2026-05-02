# Escape the Facility
Carolina Vilchez

## How to Run the Game
Open the Python file in Thonny 
Follow the prompts to play the game.

## Core Game Features
- 3 different story paths
- 3 different endings
- Inventory system
- 5 NPC interactions
- 2 challenges (guard encounter and password puzzle)
- Input validation to prevent crashes
- Audit logging system

## Story Paths
1. **Keycard Path**  
   The player searches for a keycard, encounters a guard, and tries to escape using a locked door.

2. **Hack Path**  
   The player works with a hacker and uses a password puzzle to unlock the system and escape.

3. **Scientist Path**  
   The player helps a scientist and gains access to a secret escape route.

## Endings
- **Keycard Escape** – Player defeats the guard and escapes using the key  
- **Hack Escape** – Player solves the password puzzle and escapes through the system  
- **Secret Escape** – Player helps the scientist and escapes through a hidden route  

## Locations / Events
- Office (guard encounter)
- Server Room (password puzzle)
- Lab (scientist interaction)
- Medical Room (medic NPC)
- Security Room (robot NPC)

## NPCs
- **Guard**  
  Appears in the office. The player must choose to fight or run.  
  If defeated, the player gets a key.

- **Scientist**  
  Appears in the lab. Gives the player a secret code.  

- **Hacker**  
  Appears in the server room. Gives a hacking tool.  

- **Medic**  
  Appears in the medical room. Gives a med kit.  

- **Robot**  
  Appears in the security room. Gives an access chip.  

## Inventory Items
- **Guard Key** – Used to unlock the exit door  
- **Secret Code** – Used to unlock the secret ending  
- **Hacking Tool** – Helps with hacking path  
- **Med Kit** – Support item (represents survival help)  
- **Access Chip** – Used for system access  

## Challenges
1. **Guard Encounter**  
   - Location: Office  
   - Player chooses to fight or run  
   - Success: Gain key and progress  
   - Failure: No key, harder to escape  

2. **Password Puzzle**  
   - Location: Server Room  
   - Player must enter correct password (2026)  
   - Success: Escape through system  
   - Failure: Hack fails and ending changes  

## Cyber Pack Features
- **Input Validation**  
  The game uses a safe input function to prevent crashes when users enter invalid input.

- **Audit Logging**  
  All important actions (game start, choices, challenges) are recorded in `audit_log.txt` with timestamps.

- **Save/Load & Security Concept**  
  Logging and structured input handling simulate secure system behavior and tracking user actions.
