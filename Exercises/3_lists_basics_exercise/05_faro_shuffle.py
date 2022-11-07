cards_str = input()
cards = cards_str.split(" ")
cards_shuffled = []
cards_mid = len(cards) // 2
n = int(input())

for j in range(n):
    for i in range(cards_mid):
        cards_shuffled.append(cards[i])
        cards_shuffled.append(cards[i + cards_mid])
    cards = cards_shuffled
    cards_shuffled = []

print(cards)

# https://judge.softuni.org/Contests/Compete/Index/1725#4