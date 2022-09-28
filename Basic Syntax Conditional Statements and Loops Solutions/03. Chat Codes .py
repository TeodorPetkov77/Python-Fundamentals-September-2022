n = int(input())
code = 0

for i in range(n):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code != 88 and code != 86 and code < 88:
        print("GREAT!")
    elif code > 88:
        print("Bye.")