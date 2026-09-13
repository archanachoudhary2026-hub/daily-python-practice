import random

secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
guess = int(input("Guess a number between 1 and 100: "))

if guess == secret_number:
    print("🎉 Wow, you got it right!")
elif guess < secret_number:
    print(f"Too low! The number was {secret_number}.")
else:
    print(f"Too high! The number was {secret_number}.")
