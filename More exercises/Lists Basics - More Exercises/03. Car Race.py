race_track = list(map(int, input().split(" ")))
track_middle = len(race_track) // 2 + 1

# LEFT CAR TIME:
left_car_time = 0
for stage in range(0, track_middle - 1):
    if race_track[stage] == 0:
        left_car_time *= 0.8
    else:
        left_car_time += race_track[stage]

# RIGHT CAR TIME:
right_car_time = 0
for stage in range(len(race_track) - 1, track_middle - 1, -1):
    if race_track[stage] == 0:
        right_car_time *= 0.8
    else:
        right_car_time += race_track[stage]

if right_car_time < left_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")
else:
    print(f"The winner is left with total time: {left_car_time:.1f}")