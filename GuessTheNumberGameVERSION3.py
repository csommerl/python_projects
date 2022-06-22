# Guess the number game
# Players guess a random number between 1-100
# Players have only 5 chances.


# The While loop allows the user to play again
# there is probably a better way to do this
# but I wanted to try using a for loop with a range inside a while loop

# Game selects a random number between 1 and 100
import random ## I believe that it's good practice to import packages at the top, but I might be wrong.

## It's likely you haven't gotten to defining functions, so this might be new to you?
def printInstructions():
    print(
        "WELCOME!\nTry to guess the secret number between 1 and 100\nYou only have 5 chances\nIt won't be easy!\n\n"
    )
    print('RULES.\n1.Don\'t "cheat"\n2.Don\'t "Feed The Bear"')
    print("GOOD LUCK!\n\n")

## following up on that, a lot of the different portions of the game could be extracted to helper functions.

while True: ## This is pretty standard, I think, when having a loop that's supposed to go on indefinitely.

    secret_number = str(random.randint(1, 100))

    # Intro Greeting
    printInstructions()

    # Gives the user five tries
    for tries in range(4, -1, -1):

        # Prompts user to input a number
        print("Guess a number between 1 and 100")
        guess = input()

        # Feeding the Bear kills you
        if guess.lower() == "feed the bear": ## I don't believe you need parentheses around guess, but there might be different style preferences that are taught.
            print("uh-oh!\n.........\nYou made him angry!!!!!!")
            print(
                "RRRRRRAAAAAAAAAAAAWWWWWWWWRRRRRRRRRRRRR/nGGGGGGGRRRRRRRRRROOOOOOWWWWWLLLL\nGGGGGGGGGRRRRRRRRRRRR"
                * 3
            )
            print("CHOMP")
            guess = secret_number
            user = "eaten"

        # Cheat code reveals Secret Number
        if (guess) == "cheat":
            print("********** Try guessing " + str(secret_number) + " **********.\n\n")
            user = "pumpkin eater"
            continue

        # For a correct guess, or if user is eaten by the bear, the game ends
        if (guess) == secret_number:
            if user == "eaten":
                print("UH-OH\nLooks like you were eaten.\nGAME OVER")
            elif user != "pumpkin eater":
                print("\nYOU WIN!!!!\n\nCongratulations!!!!!!!!!\n")
            else:
                print(
                    """Correct!!\nHmmmmm....You didn't CHEAT did you!?!?!? Oh well."""
                )
            break

        # For incorrect guesses
        # tells user their guess was wrong
        else:
            print("Nope. Sorry!")

        ## One reason to have helper functions is to avoid if statements following else statements like this.
        # Tells user their number of remaining attempts
        if tries > 1:
            print("\nYou have " + str(tries) + " tries remaining.\n")
            continue
        if tries == 1:
            print("\nTHIS IS YOUR LAST GUESS!!!\n\n")
            continue

        # Says Game Over after incorrect final attempt
        elif tries == 0:
            print("Sorry.\nThat was your last guess.\n\nGAME OVER!\n\n")

    # Asks Play Again? after end of game
    print("\nThanks for playing!\n\nWould you like to play again?\nyes or no?")
    play = input()

    # Responds to user and either continues or ends game
    if play != "yes":
        print("Okay. Good bye")
        break
    else:
        print(
            """
        GREAT!
        LET'S PLAY AGAIN!"""
        )
