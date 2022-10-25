numbers_list = list(map(int, input().split(" ")))
numbers_all_even = [n for n in numbers_list if n % 2 == 0]
numbers_all_odd = [n for n in numbers_list if n % 2 != 0]

command = input()

while command != "end":
    command = command.split(" ")
    if command[0] == "exchange":
        index = int(command[1])
        if index in range(len(numbers_list)):
            numbers_list = numbers_list[index + 1:len(numbers_list)] + \
                           numbers_list[0:index + 1]
        else:
            print("Invalid index")
            command = input()
            continue
    elif command[0] == "max":
        even_odd = command[1]
        if even_odd == "even":
            if not numbers_all_even:
                print("No matches")
            else:
                max_even = max(numbers_all_even)
                for num in range(len(numbers_list) - 1, -1, -1):
                    if numbers_list[num] == max_even:
                        print(num)
                        break
        elif even_odd == "odd":
            if not numbers_all_odd:
                print("No matches")
            else:
                max_odd = max(numbers_all_odd)
                for num in range(len(numbers_list) - 1, -1, -1):
                    if numbers_list[num] == max_odd:
                        print(num)
                        break
    elif command[0] == "min":
        even_odd = command[1]
        if even_odd == "even":
            if not numbers_all_even:
                print("No matches")
            else:
                min_even = min(numbers_all_even)
                for num in range(len(numbers_list) - 1, -1, -1):
                    if numbers_list[num] == min_even:
                        print(num)
                        break
        elif even_odd == "odd":
            if not numbers_all_odd:
                print("No matches")
            else:
                min_odd = min(numbers_all_odd)
                for num in range(len(numbers_list) - 1, -1, -1):
                    if numbers_list[num] == min_odd:
                        print(num)
                        break
    elif command[0] == "first":
        count = int(command[1])
        if count > len(numbers_list):
            print("Invalid count")
        else:
            temp_list = []
            if command[2] == "even":
                for n in range(len(numbers_list)):
                    if numbers_list[n] % 2 == 0:
                        temp_list.append(numbers_list[n])
                        if len(temp_list) == count:
                            break
            elif command[2] == "odd":
                for n in range(len(numbers_list)):
                    if numbers_list[n] % 2 != 0:
                        temp_list.append(numbers_list[n])
                        if len(temp_list) == count:
                            break
            print(temp_list)
    elif command[0] == "last":
        count = int(command[1])
        if count > len(numbers_list):
            print("Invalid count")
        else:
            temp_list = []
            if command[2] == "even":
                for n in range(len(numbers_list) - 1, - 1, -1):
                    if numbers_list[n] % 2 == 0:
                        temp_list.insert(0, numbers_list[n])
                        if len(temp_list) == count:
                            break
            elif command[2] == "odd":
                for n in range(len(numbers_list) - 1, - 1, -1):
                    if numbers_list[n] % 2 != 0:
                        temp_list.insert(0, numbers_list[n])
                        if len(temp_list) == count:
                            break
            print(temp_list)
    command = input()

print(numbers_list)