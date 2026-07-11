import random

def guess_game():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 10)
    attempts = 5   # total attempts

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        guess = input("Guess a number between 1 and 10: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts -= 1  # subtract attempt

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("\n🎉 YOU WON! 🎉")
            print(f"You guessed the number {number} correctly.")
            return

    
        print("\n YOU LOST ")
        print(f"The correct number was {number}.")

guess_game()