import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)

    while True:
        guess = int(input("choose a number (between 1-10): "))

        if guess < number_to_guess:
            print("number too small")
        
        elif guess > number_to_guess:
            print("number to high")
        
        else:
            print("you guessed it right! congratulations!")
            break

guess_the_number()
