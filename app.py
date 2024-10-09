import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Ask the player to guess the number
        guess = input("Enter your guess (or type 'exit' to quit): ")

        # Check if the player wants to exit
        if guess.lower() == 'exit':
            print("Thanks for playing! Goodbye!")
            break

        # Ensure the guess is a valid integer
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Provide feedback based on the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break

# Start the game
number_guessing_game()
