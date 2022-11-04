row1 = list(map(int, input().split(" ")))
row2 = list(map(int, input().split(" ")))
row3 = list(map(int, input().split(" ")))

if (sum(row1) == 6 or sum(row2) == 6 or sum(row3) == 6) \
        or (row1[0] == 2 and row2[0] == 2 and row3[0] == 2) \
        or (row1[1] == 2 and row2[1] == 2 and row3[1] == 2) \
        or (row1[2] == 2 and row2[2] == 2 and row3[2] == 2) \
        or (row1[0] == 2 and row2[1] == 2 and row3[2] == 2) \
        or (row1[2] == 2 and row2[1] == 2 and row3[0] == 2):
    print("Second player won")
elif row1[0] == 1 and row1[1] == 1 and row1[2] == 1 \
        or row2[0] == 1 and row2[1] == 1 and row2[2] == 1 \
        or row3[0] == 1 and row3[1] == 1 and row3[2] == 1 \
        or (row1[0] == 1 and row2[0] == 1 and row3[0] == 1) \
        or (row1[1] == 1 and row2[1] == 1 and row3[1] == 1) \
        or (row1[2] == 1 and row2[2] == 1 and row3[2] == 1) \
        or (row1[0] == 1 and row2[1] == 1 and row3[2] == 1) \
        or (row1[2] == 1 and row2[1] == 1 and row3[0] == 1):
    print("First player won")
else:
    print("Draw!")

# https://judge.softuni.org/Contests/Practice/Index/1726#4

# 5.	Tic-Tac-Toe
# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins, print "First player won". If the second player wins, print "Second player won". Otherwise, print "Draw!".
# Example
# Input	Output
# 2 0 1
# 0 1 0
# 1 0 2	First player won
# 0 1 0
# 2 2 2
# 1 0 0	Second player won
# 1 0 2
# 0 1 2
# 1 2 0	Draw!