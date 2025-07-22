import random

def get_player_guess():
    """
    Task for Student 1:
    1. Prompt the user to enter a number between 1 and 100.
    2. Read the input from the user.
    3. Convert the input to an integer.
    4. Return the integer.
    5. Add error handling for invalid input (e.g., text instead of a number).
    """
    # Student 1: Add your code here
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("❌ Please enter a number **between 1 and 100**.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def check_guess(secret_number, player_guess):
    """
    Task for Student 2:
    1. Compare the player's guess with the secret number.
    2. If the guess is correct, return the string "correct".
    3. If the guess is too high, return the string "high".
    4. If the guess is too low, return the string "low".
    """
    # Student 2: Add your code here
    pass

def play_game():
    """
    The main function to run the game.
    This part is already complete.
    """
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1
        guess = get_player_guess()
        result = check_guess(secret_number, guess)

        if result == "correct":
            print(f"✅ Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif result == "high":
            print("🔺 Too high! Try again.")
        elif result == "low":
            print("🔻 Too low! Try again.")
            
if __name__ == "__main__":
    play_game()
