# TODO. List comprehensions
# # squaring numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# # Write your 1 line code 👇 below:
# squared_numbers = [num ** 2 for num in numbers]
# # squared_numbers = [pow(num, 2) for num in numbers]
# # squared_numbers = [num * num for num in numbers]
# # Write your code 👆 above:
# print(squared_numbers)


# # filtering even numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# # Write your 1 line code 👇 below:
# result = [number for number in numbers if number % 2 == 0]
# # Write your code 👆 above:
# print(result)


# data overlap
# №1 solution
# with open("file1.txt") as file_1:
#     file_1_numbers = [num.strip("\n") for num in file_1.readlines()]
#
# with open("file2.txt") as file_2:
#     file_2_numbers = [num.strip("\n") for num in file_2.readlines()]
#
# result = [int(num) for num in file_1_numbers if num in file_2_numbers]
# # Write your code above 👆
# print(result)

# # №2 solution
# with open("file1.txt") as file_1:
#     file_1_numbers = file_1.readlines()
#
# with open("file2.txt") as file_2:
#     file_2_numbers = file_2.readlines()
# result = [int(num) for num in file_1_numbers if num in file_2_numbers]
# # # Write your code above 👆
# print(result)


# TODO. Dictionary comprehensions
# # Dictionary comprehension 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# result = {word: len(word) for word in sentence.split()}
# # Write your code below:
# print(result)

# Dictionary comprehension 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
