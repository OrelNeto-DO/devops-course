age = int(input("enter you'r age: "))
student = str(input("are you a student? (yes or no) "))
if age < 18 or student == "yes":
    print("you'r eligible to get a discount. check with the service provider. ")
else:
    print("you'r not eligible for a discount.")