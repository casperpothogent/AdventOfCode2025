import numpy as np

# first puzzle of day 01
# correct answer: 2285373
def calculate_sum_location_differences():
    left_locations, right_locations = convert_text_to_location_lists()

    left_locations_arr = np.asarray(sorted(left_locations))
    right_locations_arr = np.asarray(sorted(right_locations))

    abs_diff_arr = np.absolute(left_locations_arr - right_locations_arr)
    distance_sum = np.sum(abs_diff_arr)
    return distance_sum


# second puzzle of day 02
# correct answer: 21142653
def calculate_similarity_score():
    similarity_sum = 0
    left_locations, right_locations = convert_text_to_location_lists()

    for left_location in left_locations:
        similarity_sum += left_location * right_locations.count(left_location)

    return similarity_sum

# convert_text function used by both puzzles
def convert_text_to_location_lists():
    left_locations, right_list = [], []

    with open("location_lists.txt", 'r') as input_file:
        for line in input_file:
            locations = line.split()
            left_locations.append(int(locations[0]))
            right_list.append(int(locations[1]))

    return left_locations, right_list


print(calculate_sum_location_differences())
print(calculate_similarity_score())
