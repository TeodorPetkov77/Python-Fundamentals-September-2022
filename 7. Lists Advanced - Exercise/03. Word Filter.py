words = input().split(" ")

words = [i for i in words if len(i) % 2 == 0]
for i in words:
    print(i)
