shopping_list = input().split("!")

command = input()

while command != "Go Shopping!":
    command = command.split(" ")
    if command[0] == "Urgent" and command[1] not in shopping_list:
        shopping_list.insert(0, command[1])
    elif command[0] == "Unnecessary" and command[1] in shopping_list:
        shopping_list.remove(command[1])
    elif command[0] == "Correct" and command[1] in shopping_list:
        shopping_list[shopping_list.index(command[1])] = command[2]
    elif command[0] == "Rearrange" and command[1] in shopping_list:
        shopping_list.remove(command[1])
        shopping_list.insert(len(shopping_list), command[1])
    command = input()
print(", ".join(shopping_list))

# https://judge.softuni.org/Contests/Practice/Index/2031#1