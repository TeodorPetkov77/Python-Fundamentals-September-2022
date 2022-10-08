def round_list(list_str):
    list2 = []
    list1 = list_str.split(" ")
    for i in list1:
        list2.append(round(float(i)))
    return list2


numbers = input()
print(round_list(numbers))

