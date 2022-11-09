import math


def center_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})"


def center_point_not(x1, y1, x2, y2):
    if abs(x1) + abs(y1) >= abs(x2) + abs(y2):
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})"


def longest_line(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2):
    if abs(x1_1 - x2_1) + abs(y1_1 - y2_1) >= abs(x1_2 - x2_2) + abs(y1_2 - y2_2):
        print(f"{center_point(x1_1, y1_1, x2_1, y2_1)}"
              f"{center_point_not(x1_1, y1_1, x2_1, y2_1)}")
    else:
        print(f"{center_point(x1_2, y1_2, x2_2, y2_2)}"
              f"{center_point_not(x1_2, y1_2, x2_2, y2_2)}")


x1_input_1 = float(input())
y1_input_1 = float(input())
x2_input_1 = float(input())
y2_input_1 = float(input())

x1_input_2 = float(input())
y1_input_2 = float(input())
x2_input_2 = float(input())
y2_input_2 = float(input())

longest_line(x1_input_1, y1_input_1, x2_input_1, y2_input_1,
             x1_input_2, y1_input_2, x2_input_2, y2_input_2)


### WORK IN PROGRESS ### 60/100 ###