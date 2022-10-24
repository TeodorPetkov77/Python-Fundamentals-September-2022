lines = int(input())
maze = []
line_index = 0
position_index = 0
moves = 0
moves_list = []
all_routes_tested = False

# CREATE MAZE AND BORDERS 'E':

for i in range(lines):
    line_str = input()
    line = list(line_str)
    line.append('E')
    line.insert(0, 'E')
    maze.append(line)

maze.insert(0, ["E"] * len(maze[1]))
maze.append(["E"] * len(maze[1]))

# GET KATE POSITION:

for index, item in enumerate(maze):
    if "k" in item:
        line_index = index
        position_index = item.index("k")

starting_line_index = line_index
starting_position_index = position_index

while all_routes_tested is False:

    line_index = starting_line_index
    position_index = starting_position_index
    moves = 0
    for item in maze:
        for index in range(len(item)):
            if item[index] == 'X':
                item[index] = ' '

    if maze[starting_line_index - 1][starting_position_index] != ' ' and \
            maze[starting_line_index + 1][starting_position_index] != ' ' and \
            maze[starting_line_index][starting_position_index - 1] != ' ' and \
            maze[starting_line_index][starting_position_index + 1] != ' ':
        all_routes_tested = True
    maze[starting_line_index][starting_position_index] = "k"

    while True:
        if maze[line_index][position_index - 1] == ' ':
            maze[line_index][position_index - 1] = 'k'
            maze[line_index][position_index] = "X"
            moves += 1
            position_index -= 1
        elif maze[line_index][position_index - 1] == 'E':
            maze[line_index][position_index] = "X"
            maze[line_index][position_index - 1] = "#"
            moves += 1
            moves_list.append(moves)
            break
        elif maze[line_index][position_index + 1] == ' ':
            maze[line_index][position_index + 1] = 'k'
            maze[line_index][position_index] = "X"
            moves += 1
            position_index += 1
        elif maze[line_index][position_index + 1] == 'E':
            maze[line_index][position_index + 1] = '#'
            maze[line_index][position_index] = "X"
            moves += 1
            moves_list.append(moves)
            break
        elif maze[line_index - 1][position_index] == ' ':
            maze[line_index - 1][position_index] = 'k'
            maze[line_index][position_index] = "X"
            moves += 1
            line_index -= 1
        elif maze[line_index - 1][position_index] == 'E':
            maze[line_index - 1][position_index] = '#'
            maze[line_index][position_index] = "X"
            moves += 1
            moves_list.append(moves)
            break
        elif maze[line_index + 1][position_index] == ' ':
            maze[line_index + 1][position_index] = 'k'
            maze[line_index][position_index] = "X"
            moves += 1
            line_index += 1
        elif maze[line_index + 1][position_index] == 'E':
            maze[line_index + 1][position_index] = '#'
            maze[line_index][position_index] = "X"
            moves += 1
            moves_list.append(moves)
            break
        elif maze[line_index - 1][position_index] != ' ' and \
            maze[line_index + 1][position_index] != ' ' and \
            maze[line_index][position_index - 1] != ' ' and \
            maze[line_index][position_index + 1] != ' ':
            maze[line_index][position_index] = "#"
            break

if moves_list:
    print(f"Kate got out in {max(moves_list)} moves")
else:
    print("Kate cannot get out")