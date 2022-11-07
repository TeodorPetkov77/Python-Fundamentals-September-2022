happiness = list(map(int, input().split(" ")))
factor = int(input())

happiness = list(map(lambda x: x * factor, happiness))

average = sum(happiness) / len(happiness)
filtered = list(filter(lambda x: x >= average, happiness))

if len(filtered) >= len(happiness) / 2:
    print(f"Score: {len(filtered)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(happiness)}. Employees are not happy!")