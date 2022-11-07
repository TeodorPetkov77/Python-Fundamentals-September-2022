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

# Character Multiplier
# Create a program that receives two strings on a single line separated by a single space. Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum, then continue with the next two characters. If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.
# Examples
# Input	Output
# George Peter	52114
# 123 522	7647
# a aaaa	9700