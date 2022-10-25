message_string = input()
numbers_list = [int(n) for n in message_string if n.isnumeric()]
non_numbers_list = "".join([i for i in message_string if not i.isnumeric()])
take_list = [n for i, n in enumerate(numbers_list) if i % 2 == 0]
skip_list = [n for i, n in enumerate(numbers_list) if i % 2 != 0]

result_string = ""

for i in range(0, len(take_list)):
    result_string += non_numbers_list[0:take_list[i]]
    non_numbers_list = non_numbers_list[take_list[i]:len(non_numbers_list)]
    non_numbers_list = non_numbers_list[skip_list[i]:len(non_numbers_list)]

print(result_string)