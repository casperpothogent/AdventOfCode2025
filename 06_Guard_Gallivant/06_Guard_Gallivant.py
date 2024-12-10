# first puzzle of day 06
# correct answer: 5242
def count_distinct_positions_along_path():
    matrix, guard_position = convert_map_to_matrix()
    dir_index, map_done = 0, False

    while not map_done:
        map_done, guard_position, dir_index = traverse_one_step_placing_x(matrix, guard_position, dir_index)

    return sum(line.count("X") for line in matrix)


def traverse_one_step_placing_x(matrix, guard_position, dir_index):
    guard_x = guard_position[0]
    guard_y = guard_position[1]
    directions = ((-1, 0, "^"), (0, 1, ">"), (1, 0, "<"), (0, -1, "v"))

    next_x = guard_x + directions[dir_index][0]
    next_y = guard_y + directions[dir_index][1]

    if next_x < 0 or next_x >= len(matrix) or next_y < 0 or next_y >= len(matrix[0]):
        # als de guard weggelopen is van het bord
        matrix[guard_x][guard_y] = "X"
        return True, (-1, -1), -1
    elif matrix[next_x][next_y] == "#":
        dir_index = (dir_index + 1)%4
        matrix[guard_x][guard_y] = directions[dir_index][2]
        return False, (guard_x, guard_y), dir_index
    else:
        matrix[guard_x][guard_y] = "X"
        matrix[next_x][next_y] = directions[dir_index][2]
        return False, (next_x, next_y), dir_index


# second puzzle of day 06
# correct answer:



# used by both puzzles, converts map txt-file into 2-D matrix and start position of guard
def convert_map_to_matrix():
    matrix = []
    guard_x, guard_y = -1, -1
    with open("map.txt", 'r') as input_file:
        for x, line in enumerate(input_file):
            matrix.append(list(line.strip()))
            if "^" in line:
                guard_x, guard_y = x, line.index("^")

    return matrix, (guard_x, guard_y)

# used only by me to easily print the matrix and debug
def print_matrix(matrix):
    print("---- Matrix ----")
    for row in matrix:
        print("\t" + ' '.join(row))


print(count_distinct_positions_along_path())