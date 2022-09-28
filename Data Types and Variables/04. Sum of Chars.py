total = 0
n = int(input())

for i in range(n):
    letter = str(input())
    total += ord(letter)

print(f"The sum equals: {total}")