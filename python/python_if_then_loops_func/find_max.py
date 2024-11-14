def find_max(list):
    max_value = list[0]
    for number in list:
        if number > max_value:
            max_value = number
    return max_value

numbers = [1, 5, 3, 9, 2]
print(f"the max value in {numbers} is {find_max(numbers)}")