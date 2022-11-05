hood = list(map(int, input().split("@")))

command = input()
position = 0

while command != "Love!":
    command = command.split(" ")
    jump_len = int(command[1])
    position += jump_len
    if position >= len(hood):
        position = 0
    if hood[position] <= 0:
        print(f"Place {position} already had Valentine's day.")
        command = input()
        continue
    hood[position] -= 2
    if hood[position] <= 0:
        print(f"Place {position} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {position}.")

n = 0
for i in hood:
    if i > 0:
        n += 1

if sum(hood) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {n} places.")

# https://judge.softuni.org/Contests/Practice/Index/2031#2