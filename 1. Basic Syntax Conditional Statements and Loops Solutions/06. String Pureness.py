n = int(input())

for i in range(n):
    is_pure = True
    word = str(input())
    if "," in word or "." in word or "_" in word:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")