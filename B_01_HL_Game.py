def yes_no(question):

    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check if user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

def instructions():

    """Prints instructions"""
    print("""
*** Instructions ***

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses.

Good luck.
    """)

# checks for an integer more than 0 (allows <enter>)
def int_check(question, exit_code=None):

    """Asks user for game goal and makes sure it's above or equal to 13"""

    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == exit_code:
            return response

        try:
            response = int(response)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here

# Initialize game variables
mode = "regular"
rounds_played = 0


print("\n⬆️⬆️⬇️ Welcome to the Higher Lower Game 🔻🔻🔻\n")

# Instructions

want_instructions = yes_no("Do you want to see the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ", "")

if num_rounds == "":
        mode = "infinite"
        num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n*** Round {rounds_played + 1} (Infinite Mode) ***"
    else:
        rounds_heading = f"\n*** Round {rounds_played + 1} of {num_rounds} ***"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase round number
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game History / Statistics area