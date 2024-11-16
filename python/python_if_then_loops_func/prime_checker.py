import sys

def is_prime(num):
    if num <= 1:
        print("all prime numbers are greater than one")
        return False

    for i in range(2, int((num ** 0.5) +1)):
        if num % i == 0:
            return False
    print(f"the number {num} is prime")
    return True
is_prime(7)
