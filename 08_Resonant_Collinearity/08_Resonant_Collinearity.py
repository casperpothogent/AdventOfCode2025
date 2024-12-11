# first puzzle of day 08
# correct answer: 364
def count_unique_antinode_locations_puzzle01():
    antenna_dict, (rows, columns) = convert_equations_antenna_map_to_antenna_dict()
    antinodes_set = set()
    for antenna_type in antenna_dict:
        # we overlopen elke antennatype zodat we bv. nooit antinodes zoeken voor antenna A en antenna O
        for antenna1_location in antenna_dict[antenna_type]:
            for antenna2_location in antenna_dict[antenna_type]:
                # we overlopen elke combinatie van 2 gelijkaardige antennas, zodat we hun antinode kunnen berekenen
                if antenna1_location != antenna2_location:
                    anti_x = antenna2_location[0] + (antenna2_location[0] - antenna1_location[0])
                    anti_y = antenna2_location[1] + (antenna2_location[1] - antenna1_location[1])
                    if 0 <= anti_x < rows and 0 <= anti_y < columns:
                        antinodes_set.add((anti_x, anti_y))

    return len(antinodes_set)


# second puzzle of day 08
# correct answer: 1231
def count_all_antinode_locations_puzzle02():
    antenna_dict, (rows, columns) = convert_equations_antenna_map_to_antenna_dict()
    antinodes_set = set()
    for antenna_type in antenna_dict:
        # we overlopen elke antennatype zodat we bv. nooit antinodes zoeken voor antenna A en antenna O
        for antenna1_location in antenna_dict[antenna_type]:
            for antenna2_location in antenna_dict[antenna_type]:
                # we overlopen elke combinatie van 2 gelijkaardige antennas, zodat we hun antinode kunnen berekenen
                if antenna1_location != antenna2_location:
                    anti_x = antenna2_location[0]
                    anti_y = antenna2_location[1]
                    while 0 <= anti_x < rows and 0 <= anti_y < columns:
                        antinodes_set.add((anti_x, anti_y))
                        anti_x = anti_x + (antenna2_location[0] - antenna1_location[0])
                        anti_y = anti_y + (antenna2_location[1] - antenna1_location[1])

    return len(antinodes_set)


# used by both puzzles, converts equations txt-file into a list of equations without their operators
def convert_equations_antenna_map_to_antenna_dict():
    antenna_dict = {}
    rows = 0
    columns = 0
    with open("antenna_map.txt", 'r') as input_file:
        for x, line in enumerate(input_file):
            rows += 1
            for y, location in enumerate(list(line.strip())):
                if location != ".":
                    if location in antenna_dict:
                        antenna_dict[location].add((x, y))
                    else:
                        antenna_dict[location] = {(x, y)}
                columns = y+1

    return antenna_dict, (rows, columns)


print(count_unique_antinode_locations_puzzle01())
print(count_all_antinode_locations_puzzle02())