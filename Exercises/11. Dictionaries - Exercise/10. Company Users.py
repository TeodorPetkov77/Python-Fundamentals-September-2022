employees = {}
command = input()

while command != "End":
    command = command.split(" -> ")
    company = command[0]
    user = command[1]
    if company not in employees:
        employees[company] = []
    if user in employees[company]:
        command = input()
        continue
    employees[company].append(user)
    command = input()

for key, value in employees.items():
    print(f"{key}")
    for em_id in value:
        print(f"-- {em_id}")

# https://judge.softuni.org/Contests/Compete/Index/1737#9