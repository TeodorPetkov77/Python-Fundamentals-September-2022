sequence = input().split(" ")
possible_matches = len(sequence) // 2

command = input()
moves = 0

while command != "end":
    moves += 1
    command = command.split(" ")
    if int(command[0]) < 0 or int(command[0]) > len(sequence) - 1 \
            or int(command[1]) < 0 or int(command[1]) > len(sequence) - 1\
            or int(command[0]) == int(command[1]):
        sequence.insert((len(sequence) // 2), "-" + str(moves) + "a")
        sequence.insert((len(sequence) // 2), "-" + str(moves) + "a")
        print("Invalid input! Adding additional elements to the board")
        possible_matches += 1
    elif sequence[int(command[0])] == sequence[int(command[1])]:
        print(f"Congrats! You have found matching elements - "
              f"{sequence[int(command[0])]}!")
        sequence[int(command[0])] = None
        sequence[int(command[1])] = None
        sequence = [i for i in sequence if i is not None]
        possible_matches -= 1
    elif sequence[int(command[0])] != sequence[int(command[1])]:
        print("Try again!")
    if possible_matches == 0:
        break
    command = input()

if possible_matches == 0:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(sequence))