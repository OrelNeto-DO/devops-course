def even_or_odd():
    num = int(input("provide me with a number and i will check wheter is odd or even number: "))
    if num == 0:
        num = int(input("0 stands by itself and is not odd or even, you may provide me with another number instead: "))
    if num == 1:
        print("1 is an odd nubmer")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd number")

even_or_odd()