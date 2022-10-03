words1 = input().split(", ")
words2 = input().split(", ")
# new_list = []
#
# for word in words1:
#     for word1 in words2:
#         if word in word1:
#             new_list.append(word)
#             break

new_list = [word for word in words1 for word1 in words2 if word in word1]
new_list = list(dict.fromkeys(new_list))
print(new_list)