n = int(input())
total_liters = 0
for i in range(n):
    liters = int(input())
    if total_liters + liters > 255:
        print("Insufficient capacity!")
        continue
    else:
        total_liters += liters

print(total_liters)