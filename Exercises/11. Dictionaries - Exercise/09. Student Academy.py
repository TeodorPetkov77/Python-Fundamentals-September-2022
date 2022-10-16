courses = {}
command = input()

while command != "end":
    command = command.split(" : ")
    course = command[0]
    student = command[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(student)
    command = input()

for key, value in courses.items():
    print(f"{key}: {len(courses[key])}")
    for student in value:
        print(f"-- {student}")
