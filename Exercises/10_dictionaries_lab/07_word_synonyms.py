dictionary = {}
n = int(input())

for i in range(n):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)

for key, value in dictionary.items():
    print(f"{key} - {', '.join(value)}")
