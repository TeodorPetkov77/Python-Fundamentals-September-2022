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

# https://judge.softuni.org/Contests/Practice/Index/1726#2

# 3.	Car Race
# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers. Each number represents the time needed for the car to pass through that step (the index). There will be two cars. The first one starts from the left side, and the other one starts from the right side. The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time). If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.
# Example
# Input	Output
# 29 13 9 0 13 0 21 0 14 82 12	The winner is left with total time: 53.8
# Comment
# The time of the left racer is (29 + 13 + 9) * 0.8 (because of the zero) + 13 = 53.8.
# The time of the right racer is (82 + 12 + 14) * 0.8 + 21 = 107.4.
# The winner is the left racer, so we print it.
# Input	Output
# 123 20 4 0 13 0 0 5 5 14 0	The winner is right with total time: 19.2