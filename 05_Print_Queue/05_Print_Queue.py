# first puzzle of day 05
# correct answer: 5166
def sum_of_valid_update_middle_pages():
    order_dict, update_list = convert_page_orders_to_order_dict_and_update_list()
    return sum(update[len(update)//2] for update in update_list if is_update_valid(order_dict, update))


# second puzzle of day 05
# correct answer: 4679
def sum_of_invalid_update_middle_pages():
    order_dict, update_list = convert_page_orders_to_order_dict_and_update_list()
    sum_invalid_middles = 0

    for update in update_list:
        if not is_update_valid(order_dict, update):
            sum_invalid_middles += sort_incorrectly_ordered_update(order_dict, update)[len(update)//2]

    return sum_invalid_middles


def sort_incorrectly_ordered_update(order_dict, incorrect_update):
    better_order_dict = dict()
    for page in incorrect_update:
        if page in order_dict:
            better_order_dict[page] = order_dict[page].intersection(set(incorrect_update))
        else:
            better_order_dict[page] = []

    return sorted(incorrect_update, key=lambda page: -1 * len(better_order_dict[page]))

# checks whether 1 update is valid according to a dictionary that defines the order rules
def is_update_valid(order_dict, update):
    for before_page in order_dict:
        for behind_page in order_dict[before_page]:
            if (before_page in update and behind_page in update
                    # a before_page that should be before a behind_page according to a dict, cant have a higher index in the update
                    and update.index(before_page) >= update.index(behind_page)):
                return False
    return True


# input a txt file to return a dictionary that maps a page to a list of pages after it, and return a list of updates
def convert_page_orders_to_order_dict_and_update_list():
    order_dict = dict([])
    update_list = []

    with open("page_orders.txt", 'r') as input_file:
        ordering_rules_done = False
        for line in input_file:
            line = line.strip()
            if line == "":
                ordering_rules_done = True
            elif not ordering_rules_done:
                before_page = int(line.split("|")[0])
                behind_page = int(line.split("|")[1])
                if before_page in order_dict:
                    order_dict[before_page].add(behind_page)
                else:
                    order_dict[before_page] = {behind_page}
            else:
                update_list.append([int(page) for page in  line.split(",")])

    return order_dict, update_list


print(sum_of_valid_update_middle_pages())
print(sum_of_invalid_update_middle_pages())

