sum = 0
number = int(input("provide me with only positive numbers and i will count them. if you provide me with a negative number the count will stop and i will return the sum of all the positive integers: "))

while number > 0:
    sum += number   
    number = int(input("provide me with only positive numbers and i will count them. if you provide me with a negative number the count will stop and i will return the sum of all the positive integers: "))
print(f"you have provided me with a negative number", "the sum of the positive numbers is:",sum)