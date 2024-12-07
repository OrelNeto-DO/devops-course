# my_dict = {
#     "name" : "orel",
#     "age" : 25,
#     "city" : "rehovot"
# }
# print(my_dict)
# print(my_dict["name"])

# my_dict["job"] = "DevOps"

# print(my_dict)
# print(my_dict["job"])

# for value, key in my_dict.items():
#     print(f"{key} : {value}")

# my_dict.pop("city")
# print(my_dict)


# def func_name(name = "guest"):
#     print(f"hello, {name}")

# func_name()
# func_name("orel")


# def add_func(num1, num2):
#     return num1 + num2
# print(add_func(1, 2))

# def add_func_cooler(num1, num2):
#     return num1 + num2
# result = add_func(2, 3)
# print(result)


# def factorial(num):
#     result = 1
#     while num != 0:
#         result *= num  
#         num -= 1
#     return result 
# print(factorial(5))


# x = 10
# def any(anything):
#     print(x)
# any(x)

# x = 10
# def any(anything):
#     global x
#     x += 20
#     print(x)
# any(x)

# def testing_globals():
#     y = 100
#     print(y)
# testing_globals()
#probel is accsessng variable outside the func if its not global print(y)

# num1 = 10
# num2 = 50
# def two_locals():
#     return num1 + num2
# result = two_locals()
# print(result)


# my_list=[1,2,3,4,5]
# for num in my_list:
#     print(num)

# my_list = [1,2,3]
# for num in range(len(my_list)):
#     print(my_list[num])


# count = 0
# while count < 5:
#     print(count)
#     count += 1

# num_list = [10,20,30,40,50,60]
# result = 0
# for i in num_list:
#     result += i
# print(result)


# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} X {j} = {i * j}")
#     print()

# while True:
#     user_input = input("provide me with the correct input to stop (you should input 'stop'): ")
#     if user_input.lower() == "stop":
#         break



