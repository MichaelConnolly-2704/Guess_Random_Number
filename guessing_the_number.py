import random


random_number = random.randint(1,100)

attempt = 0


print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!")


def get_valid_input():
    while True:
        user_input = input("Enter your guess: ")
        if user_input.isdigit():  
            return int(user_input) 
            print("Invalid input! Please enter a number.")

while True:

    user_input = get_valid_input()

    attempt += 1

    guess = int(input("Please guess: "))


    if guess < random_number:
        print ("Your guess is too low")

    elif guess > random_number:
        print ("Your guess is too high")

    else:
        print (f" Correct!! {random_number} was the right guess")
        break
