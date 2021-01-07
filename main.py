# main.oy
# Midnight Rider
# A text-based adventure game

import sys
import textwrap
import time

INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER.

WE'VE STOLEN A CAR, WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

WE CAN'T LET THEM HAVE IT.

ONE GOAL: SURVIVAL... AND THE CAR.
REACH THE END BEFORE THE MEN GON GETCHU."""

CHOICES = """
    ----
    E. STATUS CHECK
    Q. QUIT
    ----
"""

def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

        time.sleep(1)

def main():
    #intro()

    # Variables
    done = False
    kms_travelled = 0       # 100km is the end
    agents_distance = -20   # 0 is the end
    turns = 0
    tofu = 3                # 3 is max
    fuel = 50               # 50L is max
    hunger = 0


    #MAIN LOOP
    while not done:

        #TODO: Check if reached END GAME

        #TODO: Present the user with their choices
        print(CHOICES)

        user_choice = input("WHAT DO YOU WANT TO DO?\n").lower().strip("!?,.")

        if user_choice == "e":
            print(f"\t---STATUS CHECK---")
            print(f"\tKM TRAVELLED: {kms_travelled}")
            print(f"\tFUEL REMAINING: {fuel} L")
            print(f"\tAGENTS ARE {abs(agents_distance)} KM BEHIND")
            print(f"\tYOU HAVE {tofu} TOFU LEFT")
            print(f"\t--------\n")
        elif user_choice == "q":
            done = True

        time.sleep(1.5)
        #TODO Change the environment based on user choice and RNG

        #TODO: Random event generator

    # Outro
    print("THANKS FOR PLAYING, HOPE TO SEE YOU AGAIN SOON")

if __name__ == "__main__":
    main()


