words = input().split(" ")

words = "\n".join([i for i in words if len(i) % 2 == 0])
print(words)
