students_dict = {}

command = input()

while ":" in command:
    command = command.split(":")
    student = command[0]
    student_id = command[1]
    course = command[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][student] = student_id
    command = input()

command = " ".join(command.split("_"))
for key, value in students_dict.items():
    if command == key:
        for key2, value2 in value.items():
            print(f"{key2} - {value2}")

