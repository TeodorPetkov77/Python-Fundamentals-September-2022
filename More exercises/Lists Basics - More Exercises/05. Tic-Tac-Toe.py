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
