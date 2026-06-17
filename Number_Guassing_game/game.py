import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    attempts = 10
    level = "Easy"
elif choice == 2:
    attempts = 5
    level = "Medium"
elif choice == 3:
    attempts = 3
    level = "Hard"
else:
    print("Invalid choice!") 
    exit()

print(f"\nGreat! You have selected the {level} difficulty level..")
print(f"And you have {attempts} only . ")
print("Let's start the game!\n")

number = random.randint(1, 100)

used_attempts = 0
while attempts > 0:
    guess = int(input("Enter your guess: "))
    used_attempts += 1
    

    if guess == number:
        print(
            f"\n🎉 Congratulations! You guessed the correct number "
            f"in {used_attempts} attempts."
        )
        break

    elif guess > number:
        print(f"Incorrect! The number is less than {guess}.")
     

    else:
        print(f"Incorrect! The number is greater than {guess}.")
        
    attempts -= 1
    print(f"Remaining attempts: {attempts}")
if guess != number:
    print(f"\n❌ Game Over! The number was {number}.")