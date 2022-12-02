
# rps - rock, paper, scissors
rps_opponent = {'A' : "Rock",
    'B' : "Paper",
    'C' : "Scissors"}

rps_me = {'X' : "Rock",
    'Y' : "Paper",
    'Z' : "Scissors"}

points_for_item = {"Rock" : 1,
        "Paper" : 2,
        "Scissors" : 3}

points_for_result = {"win" : 6,
        "draw" : 3,
        "lose" : 0}

part2_strategy = {'X' : "lose",
    'Y' : "draw",
    'Z' : "win"}

def process_input(input):
    for i in range(len(input)):
        input[i] = input[i].rstrip().split()

def decide_result(their_move, our_move):
    # based on a set of moves, decide the winner
    result = ""
    if their_move is 'A':
        if our_move is 'X':
            result = "draw"
        elif our_move is 'Y':
            result = "win"
        elif our_move is 'Z':
            result = "lose"
        return result
    elif their_move is 'B':
        if our_move is 'X':
            result = "lose"
        elif our_move is 'Y':
            result = "draw"
        elif our_move is 'Z':
            result = "win"
        return result
    elif their_move is 'C':
        if our_move is 'X':
            result = "win"
        elif our_move is 'Y':
            result = "lose"
        elif our_move is 'Z':
            result = "draw"
        return result
    else:
        print("unhandled moves found")

def decide_move(their_move, expected_result):
    # based on a set of moves, decide the winner
    my_move = ""
    if expected_result is 'X': #lose
        if their_move is 'A': #rock
            my_move = 'Z'
        elif their_move is 'B': #paper
            my_move = 'X'
        elif their_move is 'C': #scissors
            my_move = 'Y'
        return my_move
    elif expected_result is 'Y': #draw
        if their_move is 'A':
            my_move = 'X'
        elif their_move is 'B':
            my_move = 'Y'
        elif their_move is 'C':
            my_move = 'Z'
        return my_move
    elif expected_result is 'Z': #win
        if their_move is 'A':
            my_move = 'Y'
        elif their_move is 'B':
            my_move = 'Z'
        elif their_move is 'C':
            my_move = 'X'
        return my_move
    else:
        print("unhandled result found")

def calculate_points_for_part1(input):
    '''for given input game actions, calculate total number of points'''
    #part 1
    total_score = 0
    for this_round in input:
        opponent_move = this_round[0]
        my_move = this_round[1]
        result = decide_result(opponent_move, my_move)
        round_score = points_for_item[rps_me[my_move]] + points_for_result[result]
        total_score += round_score
    return total_score


def calculate_points_for_part2(input):
    '''for given input game actions, calculate total number of points'''
    #part 2
    total_score = 0
    for this_round in input:
        opponent_move = this_round[0]
        expected_result = this_round[1]
        my_move = decide_move(opponent_move, expected_result)
        round_score = points_for_item[rps_me[my_move]] + points_for_result[part2_strategy[expected_result]]
        total_score += round_score
    return total_score
    

if __name__ == '__main__':
    input_list = [line for line in open("C:\Work\\advent_of_code\\2022\input_files\puzzle2_input.txt", "r").readlines()]
    process_input(input_list)
    #part1
    print("part1:{}".format(calculate_points_for_part1(input_list)))
    #PART2
    print("part2:{}".format(calculate_points_for_part2(input_list)))