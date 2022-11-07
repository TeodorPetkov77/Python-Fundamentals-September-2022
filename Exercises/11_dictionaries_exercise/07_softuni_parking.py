n = int(input())
parking = {}
for i in range(n):
    command = input().split(" ")
    action = command[0]
    username = command[1]
    if action == "register":
        lic_plate = command[2]
        if username not in parking:
            parking[username] = lic_plate
            print(f"{username} registered {lic_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number "
                  f"{parking[username]}")
    elif action == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking.pop(username)

for key, value in parking.items():
    print(f"{key} => {value}")

# https://judge.softuni.org/Contests/Compete/Index/1737#6