import random
import time

number = random.randint(1,100)

guess = 0

counter = 0

while True:
    print("Guess the number between 1 and 100!")
    guess = int(input())
    counter += 1 

    if guess == number:
        print("You win!")
        print("You found the number in " + str(counter) + " guesses.")
        break 
    elif guess > number:
        print("Too high! Try again.")
    elif guess < number:
        print("Too low! Try again.")
