course_list = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    if command[0] == "Add":
        lesson_to_add = command[1]
        if lesson_to_add not in course_list:
            course_list.append(lesson_to_add)
    elif command[0] == "Insert":
        lesson_to_add = command[1]
        if lesson_to_add not in course_list:
            course_list.insert(int(command[2]), lesson_to_add)
    elif command[0] == "Remove":
        lesson_to_remove = command[1]
        if lesson_to_remove in course_list:
            course_list.remove(lesson_to_remove)
        if lesson_to_remove + "-Exercise" in course_list:
            course_list.remove(lesson_to_remove + "-Exercise")
    elif command[0] == "Swap":
        if command[1] in course_list and command[2] in course_list:
            first_item_index = course_list.index(command[1])
            second_item_index = course_list.index(command[2])
            course_list[first_item_index], course_list[second_item_index] = \
                course_list[second_item_index], course_list[first_item_index]
            if command[1] + "-Exercise" in course_list:
                course = course_list.pop(course_list.index(command[1] + "-Exercise"))
                course_list.insert(course_list.index(command[1]) + 1, course)
            if command[2] + "-Exercise" in course_list:
                course = course_list.pop(course_list.index(command[2] + "-Exercise"))
                course_list.insert(course_list.index(command[2]) + 1, course)
    elif command[0] == "Exercise":
        if command[1] in course_list and \
                command[1] + "-Exercise" not in course_list:
            exercise_to_add = command[1] + "-Exercise"
            item_index = course_list.index(command[1])
            course_list.insert(item_index + 1, exercise_to_add)
        elif command[1] not in course_list and \
                command[1] + "-Exercise" not in course_list:
            lesson_to_add = command[1]
            course_list.append(lesson_to_add)
            exercise_to_add = command[1] + "-Exercise"
            item_index = course_list.index(command[1])
            course_list.insert(item_index + 1, exercise_to_add)
    command = input()

for index, item in enumerate(course_list):
    print(f"{index + 1}.{item}")

