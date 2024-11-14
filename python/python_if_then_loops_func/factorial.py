def factorial(num):
    result = 1
    i = 1
    while i <= num:
        result *= i
        i += 1
    return result
number = int(input("provide me with a number to check his factorial: "))
print(f"the factorial result of {number} is {factorial(number)}")

