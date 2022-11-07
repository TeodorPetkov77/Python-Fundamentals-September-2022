text = "".join(input().split())
letters = {}

for letter in text:
    if letter not in letters:
        letters[letter] = 0
    letters[letter] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")

# https://judge.softuni.org/Contests/Compete/Index/1737#0