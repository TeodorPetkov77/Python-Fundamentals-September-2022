people = list(map(int, input().split(" ")))
index = 0
position = 1
executed_list = []
k = int(input())
while people:
    if index > len(people) - 1:
        index = 0
    if position % k == 0:
        executed_list.append(people.pop(index))
        position += 1
        continue
    position += 1
    index += 1

print(f"[{','.join(list(map(str, executed_list)))}]")
