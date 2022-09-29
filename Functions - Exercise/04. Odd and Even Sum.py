def sum_odd_even(a):
    odds = 0
    evens = 0
    for i in a:
        if int(i) % 2 == 0:
            evens += int(i)
        else:
            odds += int(i)
    print(f"Odd sum = {odds}, Even sum = {evens}")


number = input()
sum_odd_even(number)
