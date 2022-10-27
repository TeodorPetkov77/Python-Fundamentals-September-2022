def rage_quit(symbols: str):
    temp_string = ""
    non_num_list = []
    num_list = []
    unique = []
    result = ""
    for char in symbols:
        if not char.isnumeric():
            temp_string += char.upper()
        else:
            if temp_string:
                non_num_list.append(temp_string)
                temp_string = ""
                continue
    for char in symbols:
        if char.isnumeric():
            temp_string += char
        else:
            if temp_string:
                num_list.append(int(temp_string))
                temp_string = ""
                continue
    else:
        num_list.append(int(temp_string))
    for index in range(len(non_num_list)):
        result += non_num_list[index] * num_list[index]

    for s in symbols:
        if not s.isnumeric() and s.upper() not in unique:
            unique.append(s.upper())

    print(f"Unique symbols used: {len(unique)}")
    print(result)


rage_quit(input())

