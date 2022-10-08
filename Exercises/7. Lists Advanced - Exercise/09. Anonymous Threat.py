data_list = input().split(" ")
command = input().split()

while command != ['3:1']:
    if command[0] == "merge":
        start = int(command[1])
        end = int(command[2])
        list_lenght = len(data_list)
        if start < 0:
            start = 0
        if end >= list_lenght:
            end = list_lenght - 1
        word_to_add = ""
        for index in range(start, end + 1):
            word_to_add += data_list[index]
        data_list.insert(start, word_to_add)
        for index in range(start, end + 1):
            data_list.pop(start + 1)
        if "" in data_list:
            data_list.remove("")
    elif command[0] == "divide":
        item_to_remove = int(command[1])
        item_position = int(command[1])
        peaces = int(command[2])
        word_from_list = data_list[int(command[1])]
        peace_size = len(word_from_list) // peaces
        peaces_done = 0
        word_to_add = ""
        for index, letter in enumerate(word_from_list):
            word_to_add += letter
            if len(word_from_list) % peaces != 0 and peaces_done == peaces - 1:
                item_position += 1
                word_to_add += word_from_list[(index + 1): len(word_from_list) + 1]
                data_list.insert(item_position, word_to_add)
                break
            elif (index + 1) % peace_size == 0:
                item_position += 1
                data_list.insert(item_position, word_to_add)
                word_to_add = ""
                peaces_done += 1
        data_list.remove(data_list[item_to_remove])
    command = input().split()

print(" ".join(data_list))
