def loading(num):
    if num < 100:
        print(f"{num}% [" + "%" * (num // 10) + "."
              * (10 - (num // 10)) + "]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


number = int(input())
loading(number)