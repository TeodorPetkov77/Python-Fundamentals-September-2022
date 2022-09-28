word1 = str(input())
word2 = str(input())
word3 = ""
word_list = [word1]
n = len(word1)

for i in range(len(word1)):
    word_list.append(word3)
    word3 = word2[0:i + 1] + word1[i + 1: n]
    if word3 not in word_list:
        print(word3)