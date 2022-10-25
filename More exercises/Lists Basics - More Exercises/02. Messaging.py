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