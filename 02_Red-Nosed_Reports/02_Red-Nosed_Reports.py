import numpy as np

# first puzzle of day 01
# correct answer: 524
def count_safe_reports_without_problem_dampener():
    reports = convert_text_to_list_of_reports()
    count = sum(is_unaltered_report_safe(report) for report in reports)
    return count

# second puzzle of day 02
# correct answer: 569
def count_safe_reports_using_problem_dampener():
    reports = convert_text_to_list_of_reports()
    count_safe_reports = 0

    for report in reports:
        if is_unaltered_report_safe(report):
            # a report can already be safe, without altering it
            count_safe_reports += 1
        else:
            # or it is unsafe, and we have to consider every possibility of removing 1 level from each report
            safe_altered_reports = []
            for level_index in range(len(report)):
                altered_report = report[:level_index] + report[level_index+1:]
                safe_altered_reports.append(is_unaltered_report_safe(altered_report))
            count_safe_reports += any(safe_altered_reports)

    return count_safe_reports


# is_unaltered_report_safe gets a report as input and returns if is safe without removing any levels
# this is used directly in puzzle01, and also used to check for altered reports in puzzle02
def is_unaltered_report_safe(report):
    level_arr = np.asarray(report)
    level_difference_arr = level_arr[1:] - level_arr[:-1]

    if (# if the levels either aren't all descending or all ascending
            not ((level_difference_arr < 0).sum() == 0 or (level_difference_arr < 0).sum() == level_difference_arr.size)
        # if the difference between two adjacent levels is < 1 or > 3
            or (np.abs(level_difference_arr) < 1).sum() > 0
            or (np.abs(level_difference_arr) > 3).sum() > 0

    ):
        return False
    else:
        return True

# convert_text function used by both puzzles
def convert_text_to_list_of_reports():
    reports = []

    with open("reactor_reports.txt", 'r') as input_file:
        for line in input_file:
            report = line.split()
            report = [int(level) for level in report]
            reports.append(report)

    return reports

print(count_safe_reports_without_problem_dampener())
print(count_safe_reports_using_problem_dampener())
