# Game time
import random

# Generate a random integer between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess the number
while True: 
    try:
        guess = int(input("Guess the number between 1 and 10: "))
        break
    except ValueError:
        print("Please enter a valid number!")


guess_count = 1

# Keep asking until the user guesses correctly
while guess != secret_number:

    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    while True: 
        try:
            guess = int(input("Guess the number: "))
            break
        except ValueError:
            print("Please enter a valid number!")
    guess_count += 1 

# Display a message when the user guesses correctly
print("Congratulations! You guessed the correct number!")
print(f'The correct number was {secret_number}.')
print(f"Number of attempts: {guess_count}")

if guess_count < 5:
    print("You're awsomre!")