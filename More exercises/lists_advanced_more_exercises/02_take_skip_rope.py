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

# https://judge.softuni.org/Contests/Practice/Index/1732#1

# 2.	Take/Skip Rope
# Write a program, which reads a string and skips through it, extracting a hidden message. The algorithm you should implement is as follows:
# Let us take the string "skipTest_String044160" as an example.
# Take every digit from the string and transfer it somewhere. After this operation, you should have two lists of items - a numbers list and a non-numbers list:
# •	Numbers' list: [0, 4, 4, 1, 6, 0]
# •	Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
# After that, take every digit in the numbers list and split it up into a take list and a skip list. In the take list, you should keep all digits at an even index. In the skip list, you should keep all digits at an odd index.
# •	Numbers' list: [0, 4, 4, 1, 6, 0]
# •	Take list: [0, 4, 6]
# •	Skip list: [4, 1, 0]
# Afterward, iterate over both lists:
# •	First, take m characters from the non-numbers list and store it in a result string
# •	Then, skip n characters from the non-numbers list
# Note that the skipped characters are summed up as they go. The process would look like this:
# 1.	Current string: "skipTest_String". Take 0 characters and skip 4 characters:
# •	Taken string: ""
# •	Skipped string: "skip"
# 2.	The remaining string looks like this: "Test_String". Take 4 characters and skip 1 character:
# •	Taken string: "Test"
# •	Skipped string: "_"
# 3.	The string looks like this: "String". Take 6 characters and skip 0 characters:
# •	Taken string: "String"
# •	Skipped string: ""
# 4.	The final string is "TestString".
# After that, print the final string on the console.