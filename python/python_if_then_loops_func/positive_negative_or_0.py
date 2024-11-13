def numbers():
    num = int(input("provide me with a number and we will check if it's negative, positive or even 0!: "))
    if num == 0:
        print("the number you provided me with is equal to {num}!")
    elif num < 0:
        print("this time the number you provided me with is a negative number")
    elif num > 0:
        print("this number is positive!")
numbers()