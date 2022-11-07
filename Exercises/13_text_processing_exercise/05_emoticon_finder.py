sentence = input()
temp_emot = ""
for index in range(len(sentence)):
    if sentence[index] == ":":
        temp_emot = sentence[index] + sentence[index + 1]
        print(temp_emot)




# https://judge.softuni.org/Contests/Compete/Index/1740#4