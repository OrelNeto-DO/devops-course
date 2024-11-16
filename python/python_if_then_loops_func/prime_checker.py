# import sys

# def is_prime(num):
#     if num <= 1:
#         print("all prime numbers are greater than one")
#         return False

#     for i in range(2, int((num ** 0.5) +1)):
#         if num % i == 0:
#             print(f"the number {num} is not prime")
#             return False
#     print(f"the number {num} is prime")
#     return True

# is_prime(11)

# import sys

def is_prime(num):
    if num <= 1:
        print("all prime numbers are greater than one")
        return False

    for i in range(2, int((num ** 0.5) +1)):
        if num % i == 0:
            print(f"the number {num} is not prime")
            return False
    print(f"the number {num} is prime")
    return True

test_numbers = [7, 10, 13, 5, 7, 9, 11, 13, 15, 21, 30]
for number in test_numbers:
    print(is_prime(number))