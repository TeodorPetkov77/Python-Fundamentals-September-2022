words = input().split(" ")

words = "\n".join([i for i in words if len(i) % 2 == 0])
print(words)

# https://judge.softuni.org/Contests/Compete/Index/1731#2