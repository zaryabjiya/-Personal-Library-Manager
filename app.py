import random
import time

# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def guess_the_number():
    """Enhanced Guess the Number Game with Colors & Emojis! 🎯🎨"""

    number = random.randint(1, 100)  # Generate a secret number
    guesses_left = 7  # Total attempts

    print(f"{YELLOW}🎮 Welcome to the Ultimate Number Guessing Game! 🎉{RESET}")
    time.sleep(1)
    print(f"{BLUE}🤖 I have selected a number between 1 and 100. Can you guess it? 🔢{RESET}")

    # Game loop
    while guesses_left > 0:
        print(f"\n{RED}🔥 You have {guesses_left} attempts left.{RESET}")

        try:
            guess = int(input("🎯 Enter your guess: "))
        except ValueError:
            print(f"{RED}⚠️ Invalid input! Please enter a valid number.{RESET}")
            continue

        # Checking the guess
        if guess < number:
            print(f"{YELLOW}📉 Too low! Try again.{RESET}")
        elif guess > number:
            print(f"{YELLOW}📈 Too high! Try again.{RESET}")
        else:
            print(f"{GREEN}🎊 Congratulations! You guessed the number {number} correctly! 🎉{RESET}")
            return  # Exit if correct

        guesses_left -= 1

    # If the player runs out of guesses
    print(f"\n{RED}😢 Oops! You're out of guesses. The correct number was {number}.{RESET}")

# Start the game
guess_the_number())
