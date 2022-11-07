numbers = input().split(" ")
text = input()
message = ""

for code in range(len(numbers)):
    index = 0
    for element in numbers[code]:
        index += int(element)
        if index >= len(text):
            index = index - len(text)
    message += text[index]
    text = text[:index] + text[index + 1:]

print(message)

# https://judge.softuni.org/Contests/Practice/Index/1726#1

# 2.	Messaging
# On the first line, you will receive a sequence of numbers separated by a single space. On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string. Each char the program adds to the message should be found by its index. The index you are looking for is the sum of a number's digits from the sequence. If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index). When you find a char, you should add it to the message and remove it from the string. It means that for the following index, the text will be with one character less.
# Print the final message.
# Example
# Input	Output
# 9992 562 8933
# This is some message for you	hey
# 2 122 1123 1321 9 17211
# 87j973u59dg37e725!	judge!