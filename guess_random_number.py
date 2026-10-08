import random

number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100")

for i in range(1, 101):

    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > number:
            print("Too High!")

        elif guess < number:
            print("Too Low!")

        else:
            print("Congratulations! You guessed the number.")
            print("Number of attempts:", attempts)
            break

    except ValueError:
        print("Invalid input! Please enter a number.")