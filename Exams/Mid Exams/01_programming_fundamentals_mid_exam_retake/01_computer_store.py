command = input()
total = 0
while command != "special" and command != "regular":
    command_num = float(command)
    if command_num < 0:
        print("Invalid price!")
        command = input()
        continue
    total += command_num
    command = input()

if total == 0:
    print("Invalid order!")
else:
    taxes = total * 0.2
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    total += taxes
    if command == "special":
        total -= total * 0.1
    print(f"Total price: {total:.2f}$")
