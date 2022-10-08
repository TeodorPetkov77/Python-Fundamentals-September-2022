people = int(input())
lift_wagons = list(map(int, input().split(" ")))
lift_capacity = len(lift_wagons) * 4
lift_filled = 0 + sum(lift_wagons)
lift = 0
people_in_queue = False

while people > 0:
    if lift_capacity == lift_filled:
        if people > 0:
            people_in_queue = True
        break
    if lift_wagons[lift] == 4:
        lift += 1
        continue
    lift_wagons[lift] += 1
    lift_filled += 1
    people -= 1
if lift_capacity > lift_filled:
    print("The lift has empty spots!")
elif people_in_queue:
    print(f"There isn't enough space! {people} people in a queue!")

for i in lift_wagons:
    print(i, end=" ")

