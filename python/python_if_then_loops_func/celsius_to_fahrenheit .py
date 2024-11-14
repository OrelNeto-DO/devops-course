def celsius_to_fahrenheit():
    celsius = float(input("what degree would you like to convert? "))
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit

print("temperature in fahrenheit", celsius_to_fahrenheit())

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit

print("temperature in fahrenheit", celsius_to_fahrenheit(50))

