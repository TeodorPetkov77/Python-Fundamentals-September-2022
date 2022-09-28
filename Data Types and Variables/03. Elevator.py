import math
people = int(input())
capacity = int(input())

trips = math.ceil(people / capacity)
print(trips)