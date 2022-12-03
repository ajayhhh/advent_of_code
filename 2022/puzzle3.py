def process_input(input):
    for i in range(len(input)):
        input[i] = input[i].rstrip()

def calculate_total_points(priority_items):
    sum = 0
    for item in priority_items:
        if item.isupper(): # for upper case letters, ASCII starts from 65 to 90
            point_of_the_item = ord(item) - 38 # to get 27 for A, 28 for B and so on
        elif item.islower(): # for upper case letters, ASCII starts from 97 to 122
            point_of_the_item = ord(item) - 96 # to get 1 for a, 2 for b and so on
        sum += point_of_the_item
    return sum


def sum_of_priorities_of_items(input):
    '''sum_of_priorities_of_items'''
    #part 1
    priority_items = []
    for items in input:
        compartment1_items = items[slice(0,len(items)//2)]
        compartment2_items = items[slice(len(items)//2, len(items))]
        for idx, item in enumerate(compartment1_items):
            if item in compartment2_items:
                priority_items.append(item)
                break # its very important to find only one matching item and not continue iteration through the list after a match is found
    return calculate_total_points(priority_items)
    

def sum_of_priorities_of_items_part2(input):
    ''' sum_of_priorities_of_items_part2'''
    priority_items = []
    for idx in range(0, len(input), 3):
        if idx > (len(input) - 3): # check to not reach last two items to avoid index error
            break
        group_items1 = input[idx]
        group_items2 = input[idx+1]
        group_items3 = input[idx+2]
        for item in group_items1:
            if item in group_items2 and item in group_items3:
                priority_items.append(item)
                break # its very important to find only one matching item and not continue iteration through the list after a match is found
    return calculate_total_points(priority_items)
    

if __name__ == '__main__':
    input_list = [line for line in open("C:\Work\\advent_of_code\\2022\input_files\puzzle3_input.txt", "r").readlines()]
    process_input(input_list)
    #part1
    print("part1:{}".format(sum_of_priorities_of_items(input_list)))
    #PART2
    print("part2:{}".format(sum_of_priorities_of_items_part2(input_list)))