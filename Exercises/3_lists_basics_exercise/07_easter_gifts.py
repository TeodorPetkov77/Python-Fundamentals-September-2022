gift_str = input()
gift_list = gift_str.split(" ")

command = input()
while command != "No Money":
    command_list = command.split(" ")
    if command_list[0] == "OutOfStock":
        for i in range(len(gift_list)):
            if gift_list[i] == command_list[1]:
                gift_list[i] = None
    elif command_list[0] == "Required":
        if 0 < int(command_list[2]) < len(gift_list):
            gift_list[int(command_list[2])] = command_list[1]
    elif command_list[0] == "JustInCase":
        if gift_list[len(gift_list) - 1] is None:
            for i in range(len(gift_list) - 1, - 1, -1):
                if gift_list[i] is None:
                    continue
                else:
                    gift_list[i] = command_list[1]
                    break
        else:
            gift_list[len(gift_list) - 1] = command_list[1]
    command = input()

for i in gift_list:
    if i is None:
        continue
    else:
        print(i, end=" ")

# https://judge.softuni.org/Contests/Compete/Index/1725#6