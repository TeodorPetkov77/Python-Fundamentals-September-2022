people = list(map(int, input().split(" ")))
k = int(input())
executed = []
position = 0
index = 0
while people:
    position += 1
    if position % k == 0:
        executed_person = people.pop(index)
        executed.append(executed_person)
        continue
    index += 1
    if index > len(people) - 1:
        index = 0


print(executed)