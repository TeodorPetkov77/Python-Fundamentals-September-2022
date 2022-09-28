command = str(input())
word_to_print = ""

while command != "End":
    if command != "SoftUni":
        for i in command:
            word_to_print += i * 2
        print(word_to_print)
        word_to_print = ""
    command = str(input())