def data_types(string: str, data):
    if string == "int":
        data = int(data) * 2
    elif string == "real":
        data = f"{float(data) * 1.5:.2f}"
    elif string == "string":
        data = "$" + data + "$"
    return data


string_input = input()
data_input = input()
print(data_types(string_input, data_input))

# https://judge.softuni.org/Contests/Practice/Index/1729#3

# 1.	Data Types
# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
# •	If the data type is an int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is a string, surround the input with "$".
# Print the result on the console.
# Examples
# Input	Output
# int
# 5	10
# real
# 2	3.00
# string
# hello	$hello$
# Hint
# Try to solve the problem using only one method with different overloads.
#