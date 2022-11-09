def multiplication_sign(a, b, c):
    if a == 0 or b == 0 or c == 0:
        print("zero")
    elif (a > 0 and b > 0 and c > 0) or \
            (a < 0 and b > 0 and c < 0) or \
            (a > 0 and b < 0 and c < 0) or \
            (a < 0 and b < 0 and c > 0):
        print("positive")
    elif a < 0 or b < 0 or c < 0:
        print("negative")


num1 = int(input())
num2 = int(input())
num3 = int(input())

multiplication_sign(num1, num2, num3)
