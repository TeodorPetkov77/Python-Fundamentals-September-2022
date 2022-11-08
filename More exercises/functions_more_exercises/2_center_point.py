import math


def center_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")


x1_input = float(input())
y1_input = float(input())
x2_input = float(input())
y2_input = float(input())

center_point(x1_input, y1_input, x2_input, y2_input)

# https://judge.softuni.org/Contests/Practice/Index/1729#3

# 2.	Center Point
# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines. Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one. The resulting coordinates must be formatted to the lower integer.
# Examples
# Input	Output
# 2
# 4
# -1
# 2	(-1, 2)
# 10
# 14.5
# -17.2
# 16	(10, 14)
#