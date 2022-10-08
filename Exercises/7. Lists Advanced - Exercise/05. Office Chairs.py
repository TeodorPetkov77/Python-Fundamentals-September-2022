rooms = int(input())
total_chairs = 0
total_visitor = 0

for i in range(rooms):
    chairs_visitors = input().split(" ")
    chairs = list(chairs_visitors[0]).count("X")
    visitors = int(chairs_visitors[1])
    total_chairs += chairs
    total_visitor += visitors
    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {i + 1}")

if total_chairs >= total_visitor:
    print(f"Game On, {total_chairs - total_visitor} free chairs left")

