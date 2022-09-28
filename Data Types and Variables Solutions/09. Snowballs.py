n = int(input())
highest = -99999999999999
stored_weight = 0
stored_time = 0
stored_quality = 0

for i in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    total_value = (weight // time) ** quality
    if total_value > highest:
        highest = total_value
        stored_weight = weight
        stored_time = time
        stored_quality = quality

print(f"{stored_weight} : {stored_time} = {highest} ({stored_quality})")