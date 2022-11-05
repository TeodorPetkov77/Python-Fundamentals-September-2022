students = int(input())
lectures = int(input())
additional_bonus = int(input())
highest_attendences = 0
highest_max_bonus = 0

for i in range(students):
    attendences = int(input())
    max_bonus = attendences / lectures * (5 + additional_bonus)
    if attendences > highest_attendences:
        highest_attendences = attendences
    if max_bonus > highest_max_bonus:
        highest_max_bonus = max_bonus

print(f"Max Bonus: {round(highest_max_bonus)}.")
print(f"The student has attended {highest_attendences} lectures.")
