words = input().split(" ")
total = 0
word_1 = words[0]
word_2 = words[1]

if len(word_1) < len(word_2):
    shortest = word_1
    longest = word_2
else:
    shortest = word_2
    longest = word_1

for index in range(len(shortest)):
    total += ord(word_1[index]) * ord(word_2[index])

longest = longest[index + 1:]

for letter in longest:
    total += ord(letter)

print(total)

# https://judge.softuni.org/Contests/Compete/Index/1740#1