
def calculator():
    
    user_input = input("enter calculation: ")

    for operator in "+-*/":
        if operator in user_input:
            num1, num2 = user_input.split(operator)
            operator_found = operator
            break
    else:
        print("invalid user input") 
        return

    num1 = num1.strip()
    num2 = num2.strip()

    try:

        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
            
            print("invalid numbers. please try valid numbers")
            return
    
    if operator_found == "+":
        print(f"{num1 + num2}")
    elif operator_found == "-":
        print(f"{num1 - num2}")
    elif operator_found == "*":
        print(f"{num1 * num2}")
    elif operator_found == "/":
        if num2 == 0:
            print("cant divide by zero") #what if i want to provide another one then?
calculator()
                    
                    