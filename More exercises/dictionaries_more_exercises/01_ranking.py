def best_candidate(dictionary: dict):
    best_name = ''
    best_points = 0
    for key, value in dictionary.items():
        current_points = 0
        for key1, value1 in value.items():
            current_points += int(value1)
        if current_points > best_points:
            best_name = key
            best_points = current_points
    print(f"Best candidate is {best_name} with total {best_points} points.")


contests_passes = {}

command = input()

while command != "end of contests":
    command = command.split(":")
    contest, password = command[0], command[1]
    contests_passes[contest] = password
    command = input()

final_results = {}

command = input()

while command != 'end of submissions':
    command = command.split('=>')
    contest, password, user, points = \
        command[0], command[1], command[2], int(command[3])
    if contest in contests_passes.keys() \
            and password == contests_passes[contest]:
        if user not in final_results:
            final_results[user] = {}
        if contest not in final_results[user].keys():
            final_results[user][contest] = points
        else:
            if points > final_results[user][contest]:
                final_results[user][contest] = points
    command = input()

best_candidate(final_results)
print("Ranking:")
for key, value in sorted(final_results.items()):
    print(key)
    for key1, value1 in sorted(value.items(), key=lambda x: x[1], reverse=True):
        print(f"#  {key1} -> {value1}")


# https://judge.softuni.org/Contests/Practice/Index/1738#0

# 1.	Ranking
# Here comes the final and the most interesting part – the Final ranking of the candidate-interns. The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". Save that data because you will need it later. After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". Here is what you need to do.
# •	Check if the contest is valid (It is considered valid if you received it in the first type of input)
# •	Check if the password is correct for the given contest
# •	If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests) and the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they participated in) in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.
# Input
# •	Strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case with two equal contests
# •	Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# •	There will be no case with 2 or more users with same total points!
# Output
# •	On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
# •	Then print all students ordered as mentioned above in format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points}
# …
# #  {contestN} -> {points}"
# Constraints
# •	The strings may contain any ASCII character except from (:, =, >).
# •	The numbers will be in range [0 - 10000].
# •	Second input is always valid.
# Examples
# Input	Output
# Part One Interview:success
# JS Fundamentals:fundExam
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>Tanya=>350
# Algorithms=>fun=>Tanya=>380
# Part One Interview=>success=>Nikola=>120
# Java Basics Exam=>wrong_pass=>Teo=>400
# Part One Interview=>success=>Tanya=>220
# OOP Advanced=>password123=>Kay=>231
# C# Fundamentals=>fundPass=>Tanya=>250
# C# Fundamentals=>fundPass=>Nikola=>200
# JS Fundamentals=>fundExam=>Tanya=>400
# end of submissions	Best candidate is Tanya with total 1350 points.
# Ranking:
# Nikola
# #  C# Fundamentals -> 200
# #  Part One Interview -> 120
# Tanya
# #  JS Fundamentals -> 400
# #  Algorithms -> 380
# #  C# Fundamentals -> 350
# #  Part One Interview -> 220
# Java Advanced:funpass
# Part Two Interview:success
# Math Concept:asdasd
# Java Web Basics:forrF
# end of contests
# Math Concept=>ispass=>Monika=>290
# Java Advanced=>funpass=>Simona=>400
# Part Two Interview=>success=>Drago=>120
# Java Advanced=>funpass=>Petyr=>90
# Java Web Basics=>forrF=>Simona=>280
# Part Two Interview=>success=>Petyr=>0
# Math Concept=>asdasd=>Drago=>250
# Part Two Interview=>success=>Simona=>200
# end of submissions	Best candidate is Simona with total 880 points.
# Ranking:
# Drago
# #  Math Concept -> 250
# #  Part Two Interview -> 120
# Petyr
# #  Java Advanced -> 90
# #  Part Two Interview -> 0
# Simona
# #  Java Advanced -> 400
# #  Java Web Basics -> 280
# #  Part Two Interview -> 200