score = int(input("insert you'r score here to know wheter it is graded as a, b, c, d, e, f: "))
if score < 60:
    print("you failed the test. improve by practicing for the next time")
elif score in range(60, 69):
    print("you score is graded as: 'D'. it's a pass.")
elif score in range(70, 79):
    print("you score is graded as: 'C', you can do better!")
elif score in range(80, 89):
    print("you score is graded as: 'B'. not bad at all! well done!")
elif score in range(90, 101):
    print("you score is graded as: 'A'. well done! from here you can only rise!")


