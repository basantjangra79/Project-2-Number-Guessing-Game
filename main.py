# Number Guessing Game

import time
import random

levels = ["Easy", "Medium", "Hard"]

print("\nWelcome to Number Guessing Game!\n")

attempts = 0
max_score = 50

while True:
    try:
        for index, level in enumerate(levels, start=1):
            print(f"{index} - {level}")

        Difficulty = int(input("Enter a Number to Proceed: "))

        if Difficulty in (1, 2, 3):
            if Difficulty == 1:
                secret = random.randint(1, 50)
                level_chosed = "Easy"
                range_chosed = "1 to 50"

            elif Difficulty == 2:
                secret = random.randint(1, 100)
                level_chosed = "Medium"
                range_chosed = "1 to 100"

            if Difficulty == 3:
                secret = random.randint(1, 500)
                level_chosed = "Hard"
                range_chosed = "1 to 500"
            
            print(f"\nYou Chosed: {level_chosed} Level!, Guess The Number from {range_chosed}")

            print("Chossing a Random Number", end="")

            for i in range(5):
                print(".", end="", flush=True)
                time.sleep(0.5)

            print("\n")
        
        else:
            print("\n\nEnter a Number from 1 to 3 Only!")
            continue

        while True:
            try:
                guess = int(input("\nGuess the Number: "))
                attempts += 1

                if guess > secret:
                    print("Too High..")

                elif guess < secret:
                    print("Too Low..")

                elif guess == secret:
                    score = (max_score - attempts)/5
                    print(f"\nYou Win! Yes, You Guess the Right Number: {secret}")
                    print(f"You Score: {score}")

                    play_again = input("\nWants to Play Again ? [y/n]: ")

                    if play_again == "y":
                        break

                    elif play_again == "n":
                        print("\nSee You Next Time! Good Bye.\n\n[INFO] Game Closed by User.")
                        exit()

                    else:
                        print("\n\nOnly Answer in 'y' & 'n' ")
                        continue

                    print("="*35 + " Coded By: Basant Jangra " + "="*35)
            
            except KeyboardInterrupt:
                print("\n\nGame Closed by User.")
                exit()

            except ValueError:
                print("\n\nEnter Value as per Required Type Only.")
                continue


    except KeyboardInterrupt:
        print("\n\nGame Closed By User.")
        break

    except ValueError:
        print("\n\nEnter only Number from 1 to 3.")
        continue
