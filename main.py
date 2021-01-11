# main.py
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
REACH THE END BEFORE THE MEN GON GETCHU.
"""

WIN = """
YOU PRESSED THE BUTTON TO OPEN THE GATE.
THIS ISN'T THE FIRST TIME YOU'VE DONE THIS.
YOU CAN TIME IT PERFECTLY SO THAT YOU
SLIDE THE CAR IN AS THE GATES CLOSE.

YOU KNOW YOU DID THE RIGHT THING.
THE GOVERNMENT WOULD HAVE TORN THE CAR APART,
ANALYSING IT, TESTING IT, THEN DESTROYING IT.

THEY DON'T KNOW ITS SECRETS...
THAT IT HOLDS THE KEY TO DIFFERENT WORLDS.

AS YOU STEP OUT OF THE VEHICLE, FIDO RUNS
UP TO YOU.
"THANK YOU FOR SAVING ME," HE SAYS.

AS YOU TAKE A COUPLE OF STEPS AWAY FROM THE CAR,
IT MAKES A STRANGE NOISE.

BEFORE YOUR EYES, IT SHIFTS ITS SHAPE.
YOU'VE SEEN IT BEFORE, BUT ONLY ON TV.

"BUMBLEBEE...?"



----GAME OVER----
"""

LOSE_HUNGER = """
YOU SUCCUMBED TO YOUR HUNGER AND CANNOT CONTINUE.
THE FLASHING RED AND BLUE LIGHTS GET CLOSER AND 
CLOSER AS YOU FADE IN AND OUT OF CONSCIOUSNESS. 
THE END IS NEAR.



----GAME OVER----
"""

LOSE_AGENTS = """
THE AGENTS HAVE CLOSED IN ON YOU.
THERE ARE AT LEAST 20 CARS SURROUNDING YOU.
THE LEAD CAR BUMPS YOUR PASSENGER SIDE.
YOU MANAGE TO CORRECT YOUR STEERING
TO KEEP YOU FROM CRASHING.

YOU DIDN'T SEE THE AGENT'S CAR BESIDE YOU.
THE DRIVER BUMPS YOUR CAR.
AND THAT'S IT.

YOU SPIN UNCONTROLLABLY.
THE CAR FLIPS OVER AT LEAST TWO TIMES.
OR MORE... YOU SEEM TO HAVE LOST COUNT.

SIRENS.

"ARE THEY ALIVE?" THEY SAY AS YOU HEAR
FOOTSTEPS GETTING CLOSER.
"DOESN'T MATTER, ALL WE WANTED WAS THE CAR.

YOU SEE A DOG SLOWLY STEP OUT OF THE
OVERTURNED CAR.

"YOU WILL NEVER STOP THE REVOLUTION,"
THE DOG SEEMS TO SAY TO THE OFFICERS.

IT WAS IN THE CAR THE WHOLE TIME.

YOU DRIFT OFF INTO UNCONSCIOUSNESS.



----GAME OVER----
"""

LOSE_FUEL = """
YOUR CAR SPUTTERS AND SEEMS TO LET OUT 
A BIG SIGH. THERE'S NO MORE FUEL LEFT.

THE COPS SURROUND YOU AND THEY STEP
OUT OF THEIR CARS. THE LEAD AGENT
RIPS THE DOOR OPEN AND THROWS YOU
OUT OF THE CAR.

"WE FINALLY GOT IT"

YOU FAILED.



----GAME OVER----
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
    type_text_output(INTRODUCTION)

    # CONSTANTS
    MAX_FUEL_LEVEL = 50
    MAX_DISTANCE_TRAVELLED = 100
    MAX_TOFU = 3
    MAX_HUNGER = 50
    STARTING_AGENTS_DISTANCE = -20

    # Variables
    done = False
    kms_travelled = 0
    agents_distance = STARTING_AGENTS_DISTANCE
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
            print("******** The dog used its magic tofu cooking skills.")
        # Check if reached END GAME
        # WIN - Travelled the distance required
        # Print win scenario
        if kms_travelled > MAX_DISTANCE_TRAVELLED:
            time.sleep(2)
            type_text_output(WIN)
            break

        # LOSE - by hunger > MAX_HUNGER (50)
        elif hunger > MAX_HUNGER:
            time.sleep(2)
            type_text_output(LOSE_HUNGER)
            break

        # LOSE - agents reach you
        elif agents_distance >= 0:
            time.sleep(2)
            type_text_output(LOSE_AGENTS)
            break

        # LOSE - no fuel
        elif fuel <= 0:
            time.sleep(2)
            type_text_output(LOSE_FUEL)
            break

        # Display hunger
        if hunger > 40:
            print("******** Your stomach rumbles, you need to eat something soon.")
            time.sleep(1)
        elif hunger > 25:
            print("******** Your hunger is small, but manageable.")
            time.sleep(1)

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
            player_distance_now = random.randrange(4, 12)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(3, 7)

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
        else:
            print("\tPlease select a valid input")

        # UPKEEP
        if user_choice in ["b", "c", "d"]:
            hunger += random.randrange(8, 18)
            turns += 1

        time.sleep(1.5)

    # Outro
    print()
    print(f"You finished the game in {turns} turns.")
    print("Thanks for playing. Hope to see you again soon")

if __name__ == "__main__":
    main()