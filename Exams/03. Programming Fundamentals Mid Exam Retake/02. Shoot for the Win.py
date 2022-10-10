targets = list(map(int, input().split(" ")))
shot_targets_total = 0
command = input()

while command != "End":
    shot_target_index = int(command)
    if shot_target_index not in range(len(targets)):
        command = input()
        continue
    shot_target_value = targets[shot_target_index]
    targets[shot_target_index] = None
    shot_targets_total += 1
    for i in range(len(targets)):
        if targets[i] is None:
            continue
        elif targets[i] <= shot_target_value:
            targets[i] += shot_target_value
        elif targets[i] > shot_target_value:
            targets[i] -= shot_target_value
    command = input()

targets = list(map(lambda x: x if x is not None else -1, targets))

print(f"Shot targets: {shot_targets_total} ->", end=" ")
for i in targets:
    print(i, end=" ")