import re
import copy

def add_new_ticket_numbers(tickets, ticket_count, input, i):
    #tickets[ticket_count] = [re.split("d+", input[i])]
    num = re.split("d+", input[i])
    num = re.split(" ", num[0])
    # remove blank items from num list
    num = list(filter(None, num))
    first_num = 1
    for i in num:
        if first_num == 1:
            tickets[ticket_count] = {i : "not_found"}
            first_num = 0
        else:
            tickets[ticket_count].update({i : "not_found"})

def add_more_numbers_to_ticket(tickets, ticket_count, input, i):
    #tickets[ticket_count].append(re.split("d+", input[i]))
    num = re.split("d+", input[i])
    num = re.split(" ", num[0])
    # remove blank items from num list
    num = list(filter(None, num))
    for i in num:
        tickets[ticket_count].update({i : "not_found"})
    #tickets[ticket_count].append({num:"not_found"} for num in [re.split("d+", input[i])])

def process_input(input):
    draw = input[0].strip()
    draw = re.split(",", draw)
    tickets = {}
    ticket_count = 1
    #remove \n
    for i in range(len(input)):
        input[i] = input[i].rstrip()
    i = 1
    # create dict with bingo tickets
    while(i < len(input)):
        if input[i] == '':
            i += 1
            continue
        for j in range(1, 6):
            if j == 1:
                add_new_ticket_numbers(tickets, ticket_count, input, i)
                #tickets[ticket_count] = re.split("d+", input[i])
            else:
                add_more_numbers_to_ticket(tickets, ticket_count, input, i)
                #tickets[ticket_count].append(re.split("d+", input[i]))
            i += 1
        ticket_count += 1
    return draw , tickets

def check_for_winner(tickets):
    # sum unmarked numbers in the ticket according to the requirement
    def sum_unmarked_nums(ticket_nums):
        sum = 0
        for num, found_flag in ticket_nums.items():
            if found_flag == "not_found":
                sum += int(num)
        return sum
        
    for ticket_idx, ticket_nums in tickets.items():
        x = list(ticket_nums.values())
        if x[0] == x[1] == x[2] == x[3] == x[4] == "found": #row1
            return sum_unmarked_nums(ticket_nums)
        elif x[5] == x[6] == x[7] == x[8] == x[9] == "found": #row2 
            return sum_unmarked_nums(ticket_nums)
        elif x[10] == x[11] == x[12] == x[13] == x[14] == "found": #row3 
            return sum_unmarked_nums(ticket_nums)
        elif x[15] == x[16] == x[17] == x[18] == x[19] == "found": #row4
            return sum_unmarked_nums(ticket_nums)
        elif x[20] == x[21] == x[22] == x[23] == x[24] == "found": #row5
            return sum_unmarked_nums(ticket_nums)
        elif x[0] == x[5] == x[10] == x[15] == x[20] == "found": #col1
            return sum_unmarked_nums(ticket_nums)
        elif x[1] == x[6] == x[11] == x[16] == x[21] == "found": #col2
            return sum_unmarked_nums(ticket_nums)
        elif x[2] == x[7] == x[12] == x[17] == x[22] == "found": #col3
            return sum_unmarked_nums(ticket_nums)
        elif x[3] == x[8] == x[13] == x[18] == x[23] == "found": #col4
            return sum_unmarked_nums(ticket_nums)
        elif x[4] == x[9] == x[14] == x[19] == x[24] == "found": #col5
            return sum_unmarked_nums(ticket_nums)
        else:
            continue # no bingo in current ticket, continue to next ticket
    return 0 # no bingo in any ticket

def bingo(draw, tickets):
    '''Func1: sum of unmarked numbers multiplied by 
    number that was called last'''
    for draw_num in draw:
        draw_num = int(draw_num)
        for idx, ticket in tickets.items():
            for ticket_num, flag in ticket.items():
                #check if each number in each ticket is the drawn number
                if int(ticket_num) == draw_num:
                    ticket[ticket_num] = "found" #mark numbers found as found
        #check if there is a winner after each drawn number
        winner_sum = check_for_winner(tickets)
        if winner_sum == 0:
            continue # no bingo, continue to draw next number
        else:
            return winner_sum * draw_num # valid sum means a winner is found
    
def check_for_last_winner(tickets):
    # sum unmarked numbers in the ticket according to the requirement
    def sum_unmarked_nums(ticket_nums):
        sum = 0
        for num, found_flag in ticket_nums.items():
            if found_flag == "not_found":
                sum += int(num)
        return sum

    for ticket_idx, ticket_nums in tickets.items():
        x = list(ticket_nums.values())
        if x[0] == x[1] == x[2] == x[3] == x[4] == "found": #row1
            return sum_unmarked_nums(ticket_nums)
        elif x[5] == x[6] == x[7] == x[8] == x[9] == "found": #row2 
            return sum_unmarked_nums(ticket_nums)
        elif x[10] == x[11] == x[12] == x[13] == x[14] == "found": #row3 
            return sum_unmarked_nums(ticket_nums)
        elif x[15] == x[16] == x[17] == x[18] == x[19] == "found": #row4
            return sum_unmarked_nums(ticket_nums)
        elif x[20] == x[21] == x[22] == x[23] == x[24] == "found": #row5
            return sum_unmarked_nums(ticket_nums)
        elif x[0] == x[5] == x[10] == x[15] == x[20] == "found": #col1
            return sum_unmarked_nums(ticket_nums)
        elif x[1] == x[6] == x[11] == x[16] == x[21] == "found": #col2
            return sum_unmarked_nums(ticket_nums)
        elif x[2] == x[7] == x[12] == x[17] == x[22] == "found": #col3
            return sum_unmarked_nums(ticket_nums)
        elif x[3] == x[8] == x[13] == x[18] == x[23] == "found": #col4
            return sum_unmarked_nums(ticket_nums)
        elif x[4] == x[9] == x[14] == x[19] == x[24] == "found": #col5
            return sum_unmarked_nums(ticket_nums)
        else:
            continue # no bingo in current ticket, continue to next ticket
    return 0 # no bingo in any ticket

def bingo_last(draw, tickets):
    ''' Func2'''
    winner_sum = [0] * 100
    for draw_num in draw:
        draw_num = int(draw_num)
        for idx, ticket in tickets.items():
            for ticket_num, flag in ticket.items():
                #check if each number in each ticket is the drawn number
                if int(ticket_num) == draw_num:
                    ticket[ticket_num] = "found" #mark numbers found as found
        #check if there is a winner after each drawn number
        if winner_sum == 0:
            continue # no bingo, continue to draw next number
        else:
            winner_sum[idx]

if __name__ == '__main__':
    input_list = [line for line in open("input_files/puzzle4_input.txt", "r").readlines()]
    draw , tickets = process_input(input_list)
    draw2 = draw[:]
    tickets2 = copy.deepcopy(tickets)
    #part1
    print(bingo(draw, tickets))
    #PART2
    #print(bingo_last(draw2, tickets2))