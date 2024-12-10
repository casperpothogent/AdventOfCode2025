import math


# first puzzle of day 07
# correct answer: 10741443549536
def calculate_sum_correct_values_two_operators():
    equations_list = convert_equations_txt_to_list()
    return calculate_sum_correct_values(equations_list, False)

# second puzzle of day 07
# correct answer: 500335179214836
def calculate_sum_correct_values_three_operators():
    equations_list = convert_equations_txt_to_list()
    return calculate_sum_correct_values(equations_list, True)

def calculate_sum_correct_values(equations_list, third_operator=False):
    sum_correct_values = 0
    for equation in equations_list:
        result, numbers = equation
        sum_correct_values += result if is_equation_possible(result, numbers, third_operator) else 0
    return sum_correct_values


def is_equation_possible(result, numbers, third_operator):
    values = {numbers[0]}
    for number in numbers[1:]:
        new_values = {value + number for value in values }.union({value * number for value in values })
        if third_operator:
            new_values = new_values.union({int(str(value)+str(number)) for value in values})
        values = new_values
    return result in values


# used by both puzzles, converts equations txt-file into a list of equations without their operators
def convert_equations_txt_to_list():
    equations_list = []

    with open("faulty_equations.txt", 'r') as input_file:
        for line in input_file:
            result = int(line.split(":")[0])
            numbers = [int(number) for number in line.split(": ")[1].split(" ")]
            equations_list.append((result, numbers))

    return equations_list

print(calculate_sum_correct_values_two_operators())
print(calculate_sum_correct_values_three_operators())

