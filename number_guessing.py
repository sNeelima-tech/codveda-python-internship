import random

print("🎯 Welcome to Number Guessing Game")
print("Guess a number between 1 and 100")

number = random.randint(1, 100)
attempts = 5

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
    print("Attempts left:", attempts)
    print()

if attempts == 0:
    print("❌ Game Over!")
    print("The correct number was:", number)
