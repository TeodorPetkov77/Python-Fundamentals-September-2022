def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    print(subtract(sum_numbers(a, b), c))


num1 = int(input())
num2 = int(input())
num3 = int(input())

add_and_subtract(num1, num2, num3)