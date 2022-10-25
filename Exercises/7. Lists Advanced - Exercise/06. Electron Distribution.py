electrons = int(input())
shells = []

for i in range(1, electrons + 1):
    max_n = 2*i**2
    if electrons - max_n < 0:
        shells.append(electrons)
        break
    else:
        electrons -= max_n
        shells.append(max_n)

print(shells)

# https://judge.softuni.org/Contests/Compete/Index/1731#5