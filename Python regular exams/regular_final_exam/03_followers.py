followers = {}

command = input()

while command != 'Log out':
    command = command.split(": ")
    action = command[0]
    username = command[1]
    if action == "New follower":
        if username not in followers.keys():
            followers[username] = {"likes": 0, "comments": 0}
    elif action == "Like":
        count = int(command[2])
        if username not in followers.keys():
            followers[username] = {"likes": count, "comments": 0}
        else:
            followers[username]["likes"] += count
    elif action == "Comment":
        if username not in followers.keys():
            followers[username] = {"likes": 0, "comments": 1}
        else:
            followers[username]["comments"] += 1
    elif action == "Blocked":
        if username in followers.keys():
            followers.pop(username)
        else:
            print(f"{username} doesn't exist.")
    command = input()

print(f"{len(followers)} followers")
for key, value in followers.items():
    print(f"{key}: {value['likes'] + value['comments']}")