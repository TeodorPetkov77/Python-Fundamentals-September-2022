divisible = int(input())
bound = int(input())

for i in range(bound, -1, -1):
    if i % divisible == 0:
        print(i)
        break

