import random

print("Guessing Game 1-9")

number = random.randint(1, 9)

chances = 0

print("Choose a number (between 1 and 9):")

while chances < 5:

    guess = int(input("Enter your guess:- "))

    if guess == number:
        print("Congratulations! You Win!")
        break

    elif guess < number:
        print("Your number is too low. Choose a number that's higher than", guess)

    else:
        print("Your number is too high. Choose a number that's lower than", guess)

    chances += 1

if not chances < 5:
    print("You Lost to a Computer... The number was", number)