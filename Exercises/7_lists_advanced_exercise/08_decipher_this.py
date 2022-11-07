message = input().split(" ")

for word in message:
    code = "".join([i for i in word if i.isnumeric()])
    letters = [i for i in word if i.isalpha()]
    letters[0], letters[len(letters) - 1] = letters[len(letters) - 1], letters[0]
    letters = "".join(letters)
    print(f"{chr(int(code))}{letters}", end=" ")

# https://judge.softuni.org/Contests/Compete/Index/1731#7