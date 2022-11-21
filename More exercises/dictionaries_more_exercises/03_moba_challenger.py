def check_match(person_1, person_2, dictionary: dict):
    match = False
    for key in dictionary[person_1].keys():
        if key in dictionary[person_2].keys():
            match = True
            break
    return match


moba = {}

command = input()

while command != "Season end":
    if '->' in command:
        command = command.split(' -> ')
        name = command[0]
        position = command[1]
        points = int(command[2])
        if name not in moba.keys():
            moba[name] = {position: points}
        else:
            if position not in moba[name].keys():
                moba[name][position] = points
            if moba[name][position] < points:
                moba[name][position] = points
    else:
        command = command.split(' vs ')
        name_1 = command[0]
        name_2 = command[1]
        if name_1 in moba and name_2 in moba and \
                check_match(name_1, name_2, moba):
            name_1_total = (sum(moba[name_1].values()))
            name_2_total = (sum(moba[name_2].values()))
            if name_1_total > name_2_total:
                moba.pop(name_2)
            elif name_2_total > name_1_total:
                moba.pop(name_1)
    command = input()

for key, value in sorted(moba.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f'{key}: {(sum(moba[key].values()))} skill')
    for key1, value1 in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f'- {key1} <::> {value1}')

# https://judge.softuni.org/Contests/Practice/Index/1738#2

# 3.	MOBA Challenger
# You are a pro MOBA player, you are struggling to become а master of the Challenger tier. So, you carefully watch the statistics in the tier.
# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number. You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, if he isn`t present, else add his position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# •	If they got at least one position in common, the player with better total skill points wins and the other is demoted from the tier -> remove him.
# •	If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
# •	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end". At that point you should print the players, ordered by total skill in descending order, then ordered by player name in ascending order. For each player print their position and skill, ordered descending by skill, then ordered by position name in ascending order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Player and position will always be one word string, containing no whitespaces.
# •	Skill will be an integer in the range [0, 1000].
# •	There will be no invalid input lines.
# •	The program ends when you receive the command "Season end".
# Output
# •	The output format for each player is:
# "{player}: {total_skills} skill"
# - {position1} <::> {skill}
# - {position2} <::> {skill}
# …
# - {positionN} <::> {skill}"
# Examples
# Input	Output	Comments
# Peter -> Adc -> 400
# George -> Jungle -> 300
# Simon -> Mid -> 200
# Simon -> Support -> 250
# Season end	Simon: 450 skill
# - Support <::> 250
# - Mid <::> 200
# Peter: 400 skill
# - Adc <::> 400
# George: 300 skill
# - Jungle <::> 300	We order the players by total skill points descending, then by name. We print every position along its skill ordered descending by skill, then by position name.
# Peter -> Adc -> 400
# Bush -> Tank -> 150
# Frank -> Mid -> 200
# Frank -> Support -> 250
# Frank -> Tank -> 250
# Peter vs Frank
# Frank vs Bush
# Frank vs Hide
# Season end	Frank: 700 skill
# - Support <::> 250
# - Tank <::> 250
# - Mid <::> 200
# Peter: 400 skill
# - Adc <::> 400	Frank and Peter don`t have common position, so the duel isn`t valid.
# Frank wins vs Bush /common position: "Tank". Bush is demoted.
# Hide doesn`t exist so the duel isn`t valid.
# We print every player left in the tier.