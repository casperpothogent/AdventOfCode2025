import re

# first puzzle of day 03
# correct answer: 187825547
def sum_of_correct_multiplications():
    muls = convert_text_to_list_of_muls()
    return sum(calculate_value_of_mul(mul) for mul in muls)


# second puzzle of day 03
# correct answer: 85508223
def sum_of_multiplications_with_conditional_statements():
    instructions = convert_text_to_list_of_instructions()
    sum_of_muls, previous_instruction = 0, "do"

    for instruction in instructions:
        if instruction == "do" or instruction == "don't":
            previous_instruction = instruction
        elif previous_instruction == "do":
            sum_of_muls += calculate_value_of_mul(instruction)

    return sum_of_muls

# used only puzzle 01, finds only valid muls in the txt file
def convert_text_to_list_of_muls():
    muls = []

    with open("corrupted_memory.txt", 'r') as input_file:
        for line in input_file:
            muls += re.findall(r"mul\([0-9]+,[0-9]+\)", line)

    return muls

# used only by puzzle02, collects all occurences of "do", "don't" or any muls into a list
def convert_text_to_list_of_instructions():
    instructions = []

    with open("corrupted_memory.txt", 'r') as input_file:
        for line in input_file:
            instructions += re.findall(r"mul\([0-9]+,[0-9]+\)|don't|do", line)

    return instructions

# used my both puzzles, calculates the value of a mul
# for example:  calculate_value_of_mul("mul(1,4)") -> return 4
def calculate_value_of_mul(mul):
    numbers = mul[4:-1].split(',')
    return int(numbers[0]) * int(numbers[1])

print(sum_of_correct_multiplications())

print(sum_of_multiplications_with_conditional_statements())
