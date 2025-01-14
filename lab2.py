# Due: Sunday night at midnight
#
# Define a new array called weapons and add 6 different weapon names in the array,
# with increasing levels of weapon strength. Use Fist, Knife, Club, Gun, Bomb, Nuclear bomb
# Roll the dice (1-6) to choose which weapon you must use.
# Save the roll in a variable called weaponRoll.
# Add your weaponRoll to the hero's combat strength
# Use this variable as an index into the weapons array and print out the name of the hero's weapon.
#  Define the following condition:
# If weaponRoll is less than or equal to 2, print out "You rolled a weak weapon, friend".
# But if weaponRoll is less than or equal to 4, print out "Your weapon is meh"
# Else, print out "Nice weapon, friend! "
# If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
# Add error handling on all inputs eg. if input is not int, print an error message and halt
import random

try:
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
    weaponRoll = random.randint(1, 6)
    print(weapons[weaponRoll-1])
    if weaponRoll <=2:
        print("You rolled a weak weapon, friend")
        if weaponRoll-1 != 0:
            print("Thank goodness you didn't roll the Fist...")
    elif weaponRoll <=4:
        print("Your weapon is meh")
        print("Thank goodness you didn't roll the Fist...")
    else:
        print("Nice weapon, friend!")
        print("Thank goodness you didn't roll the Fist...")
except Exception as e:
    print("An error occurred:", e)



