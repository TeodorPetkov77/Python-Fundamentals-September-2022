money = input()
money_list = money.split(", ")
money_list_int = []
beggars = int(input())
beggars_str = beggars * "0 "
beggars_list = beggars_str.split(" ")
beggars_list = beggars_list[0:beggars]
beggars_list_int = []
x = 0

for i in beggars_list:
    beggars_list_int.append(int(i))

for i in money_list:
    money_list_int.append(int(i))

for i in money_list_int:
    if x == beggars:
        x = 0
    beggars_list_int[x] += i
    x += 1

print(beggars_list_int)

# https://judge.softuni.org/Contests/Compete/Index/1725#2