def add_and_subtract(a, b, c):
    def sum_numbers():
        return a + b

    def subtract():
        print(sum_numbers() - c)
    sum_numbers()
    subtract()


num1 = int(input())
num2 = int(input())
num3 = int(input())

add_and_subtract(num1, num2, num3)