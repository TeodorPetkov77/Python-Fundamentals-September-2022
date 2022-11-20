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


contests_dictionary = {}
while True:
    contest_info = input().split(":")
    if len(contest_info) <= 1:
        break
    contest = contest_info[0]
    password = contest_info[1]
    contests_dictionary[contest] = password
participant_submission_dictionary = {}
while True:
    submission_info = input().split("=>")
    if len(submission_info) <= 1:
        break
    contest = submission_info[0]
    password = submission_info[1]
    username = submission_info[2]
    points = int(submission_info[3])
    for key, value in contests_dictionary.items():
        if contest == key and password == value:
            if username not in participant_submission_dictionary.keys():
                participant_submission_dictionary[username] = {}
            if contest not in participant_submission_dictionary[username].keys() or \
                    points > participant_submission_dictionary[username][contest]:
                participant_submission_dictionary[username][contest] = points

best_candidate(participant_submission_dictionary)

print('Ranking:')
for user in sorted(participant_submission_dictionary.keys()):
    print(f'{user}')
    participant_submission_dictionary[user] = dict(
        sorted(participant_submission_dictionary[user].items(), key=lambda x: x[1], reverse=True))
    for contest, points in participant_submission_dictionary[user].items():
        print(f'#  {contest} -> {points}')

