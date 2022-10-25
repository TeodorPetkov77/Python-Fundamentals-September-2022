numbers = list(map(int, input().split(", ")))
group = 0
while len(numbers) > 0:
    group += 10
    numbers_group = list(filter(lambda x: group - 10 < x <= group, numbers))
    numbers = [y for y in numbers if y not in numbers_group]
    print(f"Group of {group}'s: {numbers_group}")

# https://judge.softuni.org/Contests/Compete/Index/1731#6
