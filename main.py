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

def main():
    pass

    #TODO: Display introduction
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


    #MAIN LOOP
        #TODO: Check if reached END GAME

        #TODO: Present the user with their choices

        #TODO Change the environment based on user choice and RNG

        #TODO: Random event generator
if __name__ == "__main__":
    main()


