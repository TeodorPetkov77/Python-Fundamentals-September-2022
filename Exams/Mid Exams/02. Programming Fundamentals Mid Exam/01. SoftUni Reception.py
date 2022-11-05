employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students = int(input())

total_effi_h = employee1 + employee2 + employee3
hours = 0

while students > 0:
    hours += 1
    if hours != 0 and hours % 4 == 0:
        hours += 1
    students -= total_effi_h


print(f"Time needed: {hours}h.")