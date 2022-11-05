def find_composer(piece, dict):
    for key, value in dict.items():
        if key == piece:
            for key1 in value.keys():
                comp = key1
                return comp


pieces = int(input())
piece_dictionary = {}

for i in range(pieces):
    piece_composer_key = input().split("|")
    piece = piece_composer_key[0]
    composer = piece_composer_key[1]
    piece_key = piece_composer_key[2]
    if piece not in piece_dictionary:
        piece_dictionary[piece] = {composer: piece_key}

command = input()

while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        piece_key = command[3]
        if piece not in piece_dictionary:
            piece_dictionary[piece] = {composer: piece_key}
            print(f"{piece} by {composer} in {piece_key} "
                  f"added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in piece_dictionary:
            piece_dictionary.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} "
                  f"does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in piece_dictionary:
            composer = find_composer(piece, piece_dictionary)
            piece_dictionary[piece][composer] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} "
                  f"does not exist in the collection.")
    command = input()

for key, value in piece_dictionary.items():
    for key1, value1 in value.items():
        print(f"{key} -> Composer: {key1}, Key: {value1}")