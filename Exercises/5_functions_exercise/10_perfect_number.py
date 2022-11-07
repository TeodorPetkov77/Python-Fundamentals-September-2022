def perfect_num(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_num(number)