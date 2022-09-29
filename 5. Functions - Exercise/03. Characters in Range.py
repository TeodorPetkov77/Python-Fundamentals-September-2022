def char_range(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


char1 = input()
char2 = input()

char_range(char1, char2)
