print("lets see if you are eligible to drive")

age = int(input("what is you'r age? "))
if age >= 18:
    print("you are old enough to drive!")
elif age in range(15, 17): 
    print("almost there!")
else:
    print("you are not old enough to drive yet")