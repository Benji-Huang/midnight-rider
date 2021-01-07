# main.oy
# Midnight Rider
# A text-based adventure game

import random
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

WIN = """
YOU PRESSED THE BUTTON TO OPEN THE GATE. 
THIS ISN'T THE FIRST TIME YOU'VE DONE THIS.
YOU CAN TIME IT PERFECTLY SO THAT YOU 
SLIDE THE CAR IN AS THE GATES CLOSE.

YOU KNOW YOU DID THE RIGHT THING.
THE GOVERNMENT WOULD HAVE TORN THE CAR APART,
ANALYSING IT, TESTING IT, THEN DESTROYING IT.

THEY DON'T KNOW ITS SECRETS...

AS YOU STEP OUT OF THE VEHICLE, FIDO RUNS 
UP TO YOU
"THANK YOU FOR SAVING ME," HE SAYS.

AS YOU TAKE A COUPLE STEPS
"""

CHOICES = """
    ----
    A. EAT A PIECE OF TOFU
    B. DRIVE AT A MODERATE SPEED
    C. DRIVE FULL THROTTLE
    D. STOP TO REFUEL (NO FOOD AVAILABLE)
    E. STATUS CHECK
    Q. QUIT
    ----
"""

def type_text_output(string):
    for char in textwrap.dedent(string):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)

def main():
    #type_text_output(INTRODUCTION)

    # Constants
    MAX_FUEL_LEVEL = 50
    MAX_DISTANCE_TRAVELLED = 100
    MAX_TOFU = 3

    # Variables
    done = False
    kms_travelled = 0
    agents_distance = -20   # 0 is the end
    turns = 0
    tofu = MAX_TOFU
    fuel = MAX_FUEL_LEVEL
    hunger = 0

    #MAIN LOOP
    while not done:
        # Random events
        # FIDO - refills your food (5%)
        if tofu < 3 and random.random() < 0.05:
            # Refill tofu
            tofu = MAX_TOFU
            # Player feedback
            print("******** You look at your tofu container.")
            print("******** It is filled magically.")
            print("******** \"You're welcome\", says a small voice.")
            print("******** The dog used its magic tofu cooking skills0.")
        # Check if reached END GAME
        # WIN - Travelled the distance required
        # Print win scenario
        if kms_travelled > MAX_DISTANCE_TRAVELLED:
            time.sleep(2)
            type_text_output(WIN)
            # Break loop
            break

    # Display the user their choices
        print(CHOICES)

        user_choice = input("WHAT DO YOU WANT TO DO?\n").lower().strip("!?,.")

        if user_choice == "a":
            # Eat/Hunger
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- Mmmmmmm, soybean goodness.")
                print("YOUR HUNGER IS SATED")
                print()
            else:
                print()
                print("-------- YOU DON'T HAVE ANY TOFU")
                print()

        elif user_choice == "b":
            # Moderate speed
            player_distance_now = random.randrange(7, 10)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= 5

            # Player distance travelled
            kms_travelled += player_distance_now

            # Agent distance travelled
            agents_distance -= player_distance_now - agents_distance_now

            # Feedback to player
            print()
            print(f"-------- YOU TRAVELED {player_distance_now} KM.")
            print()

        elif user_choice == "c":
            # FAST
            player_distance_now = random.randrange(9, 16)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(7, 11)

            # Player distance travelled
            kms_travelled += player_distance_now

            # Agent distance travelled
            agents_distance -= player_distance_now - agents_distance_now

            # Feedback to player
            print()
            print("ZOOOOOOOOM")
            print(f"-------- YOU TRAVELED {player_distance_now} KM.")
            print()

        elif user_choice == "d":
            # Refueling
            # Fill up the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give player feedback
            print()
            print("-------- YOU FILLED THE FUEL TANK")
            print("-------- THE AGENTS GOT CLOSER...")
            print()

        elif user_choice == "e":
            # Display status of game
            print(f"\t---STATUS CHECK---")
            print(f"\tKM TRAVELLED: {kms_travelled}")
            print(f"\tFUEL REMAINING: {fuel} L")
            print(f"\tAGENTS ARE {abs(agents_distance)} KM BEHIND")
            print(f"\tYOU HAVE {tofu} TOFU LEFT")
            print(f"\t--------\n")

        elif user_choice == "q":
            done = True
        # Hunger
        if user_choice not in ["a", "e"]:
            hunger += random.randrange(5, 13)

        time.sleep(1.5)

    # Outro
    print("THANKS FOR PLAYING, HOPE TO SEE YOU AGAIN SOON")

if __name__ == "__main__":
    main()