word1 = input()
word2 = input()

while word1 in word2:
    word2 = word2.replace(word1, "")

print(word2)