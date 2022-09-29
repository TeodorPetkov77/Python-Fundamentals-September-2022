def calculate(num1, num2, operator):
    result = None
    if operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    elif operator == "divide":
        result = num1 // num2
    elif operator == "multiply":
        result = num1 * num1
    return result


input_operator = input()
first_num = int(input())
second_num = int(input())

print(calculate(first_num, second_num, input_operator))
