# Generate a random number between 1 and 100
import random
secret_number = random.randint(1, 100)
attempts = 0
print("🎉 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")
while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again. 🔽")
        elif guess > secret_number:
            print("Too high! Try again. 🔼")
        else:
            print(f"🎊 Congratulations! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("⚠️ Please enter a valid number.")
'''op
🎉 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100. Can you guess it?
Enter your guess: 89
Too high! Try again. 🔼
Enter your guess: 54
Too high! Try again. 🔼
Enter your guess: 1
Too low! Try again. 🔽
Enter your guess: 45
Too high! Try again. 🔼
Enter your guess: 34
🎊 Congratulations! You guessed it in 5 attempts.'''
