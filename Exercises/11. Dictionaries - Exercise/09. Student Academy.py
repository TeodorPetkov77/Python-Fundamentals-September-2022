n = int(input()) * 2
final_grades = {}

for i in range(1, n + 1):
    stud_grade = input()
    if i % 2 != 0:
        student = stud_grade
        if stud_grade not in final_grades:
            final_grades[student] = []
    else:
        grade = float(stud_grade)
        final_grades[student].append(grade)

final_grades = {key: sum(value) / len(value) for key, value in final_grades.items()
                if sum(final_grades[key]) / len(final_grades[key]) >= 4.5}

for key, value in final_grades.items():
    print(f"{key} -> {value:.2f}")