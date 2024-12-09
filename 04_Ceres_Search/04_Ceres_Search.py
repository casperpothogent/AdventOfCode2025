
# first puzzle of day 01
# correct answer: 2599
def search_matrix_for_xmas():
    matrix = convert_word_search_to_matrix()
    sum_of_xmas = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == "X":
                sum_of_xmas += count_xmas_starting_from_position(x, y, matrix)

    return sum_of_xmas

# second puzzle of day 01
# correct answer: 1948
def search_matrix_for_double_mas():
    matrix = convert_word_search_to_matrix()
    sum_of_double_mas = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == "A":
                sum_of_double_mas += count_double_mas_starting_from_position_A(x, y, matrix)

    return sum_of_double_mas

# used by puzzle 01
# knowing that matrix[x,y] is an "X", this function looks at all XMAS's starting here, going in all 8 directions
def count_xmas_starting_from_position(x, y, matrix):
    sum_of_xmas = 0
    possible_directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not x == y == 0]

    for direction in possible_directions:
        i = direction[0]
        j = direction[1]
        if not (0 <= x + 3*i < len(matrix)) or not (0 <= y + 3*j < len(matrix[0])):
            # if according to current direction, the last letter "S" would exceed the indices of the matrix, we don't check this direction
            sum_of_xmas += 0
        else:
            sum_of_xmas += matrix[x + 1*i][y + 1*j] == "M" and matrix[x + 2*i][y + 2*j] == "A" and matrix[x + 3*i][y + 3*j] == "S"

    return sum_of_xmas

# used by puzzle 02
# assuming that matrix[x,y] is an "A", this function looks for the needed shape with this position as the center
def count_double_mas_starting_from_position_A(x, y, matrix):
    sum_of_double_mas = 0
    #if not
    if x == 0 or  x == len(matrix) - 1 or y == 0 or  y == len(matrix[0]) - 1:
        # if A is on the edge of the matrix, double MAS will never be possible
        sum_of_double_mas += 0
    else:
        mas1_correct = (matrix[x-1][y-1] in ("M", "S") and matrix[x+1][y+1] in ("M", "S")
                        and matrix[x-1][y-1] != matrix[x+1][y+1])
        mas2_correct = (matrix[x-1][y+1] in ("M", "S") and matrix[x+1][y-1] in ("M", "S")
                        and matrix[x-1][y+1] != matrix[x+1][y-1])
        sum_of_double_mas += mas1_correct and mas2_correct
    return sum_of_double_mas


# used by both puzzles, converts txt-file to 2D-matrix
def convert_word_search_to_matrix():
    matrix = []

    with open("word_search.txt", 'r') as input_file:
        for line in input_file:
            matrix.append(list(line.strip()))

    return matrix


print(search_matrix_for_xmas())
print(search_matrix_for_double_mas())