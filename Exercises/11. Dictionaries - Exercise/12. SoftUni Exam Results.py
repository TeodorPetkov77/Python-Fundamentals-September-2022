judge_exams = {}
entry_list = []
command = input()

while command != "exam finished":
    command = command.split("-")
    username = command[0]
    language = command[1]
    if language != "banned":
        entry_list.append(language)
    if username in judge_exams and command[1] == "banned":
        judge_exams[username][1]["banned"] = "yes"
        command = input()
        continue
    points = int(command[2])
    if username not in judge_exams:
        judge_exams[username] = []
        judge_exams[username].append({"max_points": 0})
        judge_exams[username].append({"banned": "no"})
    judge_exams[username].append({language: points})
    if points > judge_exams[username][0]["max_points"]:
        judge_exams[username][0]["max_points"] = points
    command = input()

print("Results:")
for key in judge_exams.keys():
    banned = False
    for value in judge_exams[key]:
        if value == {"banned": "yes"}:
            banned = True
            break
    if banned is False:
        print(f"{key} | {judge_exams[key][0]['max_points']}")

print("Submissions:")
for lan in dict.fromkeys(entry_list):
    n = entry_list.count(lan)
    print(f"{lan} - {n}")

