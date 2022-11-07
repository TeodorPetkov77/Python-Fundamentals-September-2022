def factorial(num1, num2):
    factorial1 = num1
    factorial2 = num2
    for i in range(1, num1):
        factorial1 = factorial1 * i
    for i in range(1, num2):
        factorial2 = factorial2 * i
    print(f"{factorial1 / factorial2:.2f}")


number1 = int(input())
number2 = int(input())

factorial(number1, number2)
