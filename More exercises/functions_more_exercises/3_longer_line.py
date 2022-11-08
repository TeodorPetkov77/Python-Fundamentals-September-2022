import math

### WORK IN PROGRESS ### 40/100

def longest_line(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2):
    if abs(x1_1) + abs(y1_1) + abs(x2_1) + abs(y2_1) >= \
            abs(x1_2) + abs(y1_2) + abs(x2_2) + abs(y2_2):
        print(f"({math.floor(x2_1)}, {math.floor(y2_1)})"
              f"({math.floor(x1_1)}, {math.floor(y1_1)})")
    else:
        print(f"({math.floor(x2_2)}, {math.floor(y2_2)})"
              f"({math.floor(x1_2)}, {math.floor(y1_2)})")


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

### WORK IN PROGRESS ### 40/100