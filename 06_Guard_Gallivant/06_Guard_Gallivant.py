# first puzzle of day 06
# correct answer: 5242
def count_distinct_positions_along_path():
    matrix, guard_position = convert_map_to_matrix()
    dir_index, map_done = 0, False
    traversed_positions = set()

    while not map_done:
        map_done, guard_position, dir_index = traverse_one_step(matrix, guard_position, dir_index)
        traversed_positions.add(guard_position)

    return len(traversed_positions)

# second puzzle of day 06
# correct answer: 1424
def count_loop_causing_obstacles():
    matrix, guard_position = convert_map_to_matrix()
    dir_index, map_done = 0, False
    sum_loops = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if (x, y) != guard_position and matrix[x][y] == ".":
                print("poging: " + str(x) + ", " + str(y))
                sum_loops += check_if_obstacle_causes_loop(matrix, guard_position, dir_index, (x, y))
    return sum_loops


# checks if placing an obstacle at obstacle_position would cause a loop
def check_if_obstacle_causes_loop(matrix, guard_position, dir_index, obstacle_position):
    map_done = False
    matrix_copy = [row[:] for row in matrix]
    traversed_positions_and_direction = set()

    matrix_copy[obstacle_position[0]][obstacle_position[1]] = "#"
    while not map_done:
        map_done, guard_position, dir_index = traverse_one_step(matrix_copy, guard_position, dir_index)
        if (guard_position, dir_index) in traversed_positions_and_direction:
            return True
        else:
            traversed_positions_and_direction.add((guard_position, dir_index))

    return False

def traverse_one_step(matrix, guard_position, dir_index):
    guard_x, guard_y = guard_position
    directions = ((-1, 0, "^"), (0, 1, ">"), (1, 0, "<"), (0, -1, "v"))

    next_x = guard_x + directions[dir_index][0]
    next_y = guard_y + directions[dir_index][1]

    if next_x < 0 or next_x >= len(matrix) or next_y < 0 or next_y >= len(matrix[0]):
        # als de guard weggelopen is van het bord
        return True, (-1, -1), -1
    elif matrix[next_x][next_y] == "#":
        #als de guard een obstakel tegenkomt ddraait hji hem maar hij verplaatst hem niet
        dir_index = (dir_index + 1)%4
        return False, (guard_x, guard_y), dir_index
    else:
        # andere verplaatst de guard hem gewoon in huidige richting
        return False, (next_x, next_y), dir_index


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


print(count_distinct_positions_along_path())
print(count_loop_causing_obstacles())