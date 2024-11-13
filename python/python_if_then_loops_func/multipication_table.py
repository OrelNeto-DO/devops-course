number = int(input("provide me with a number and we will calculate it's multipicatoin options between 1-10: "))
for i in range(1, 11):
    result = number * i
    print(f"{number} X {i} = {result}")