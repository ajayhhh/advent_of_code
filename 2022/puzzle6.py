def process_input(input):
    for i in range(len(input)):
        input[i] = input[i].rstrip()
        
def find_marker(input):
    '''find_marker'''
    #part 1
    for i in range(len(input[0])):
        if input[0][i] != input[0][i+1] and input[0][i] != input[0][i+2] and input[0][i] != input[0][i+3] and input[0][i+1] != input[0][i+2] and input[0][i+1] != input[0][i+3] and input[0][i+2] != input[0][i+3]:
            return i+4

def find_marker_part2(input):
    ''' Func2'''
    for i in range(len(input[0])):
        moving_window = input[0][i:i+14]
        if len(set(moving_window)) != 14:
            continue
        return i+14
    

if __name__ == '__main__':
    input_seq = [line for line in open("C:\Work\\advent_of_code\\2022\input_files\puzzle6_input.txt", "r").readlines()]
    process_input(input_seq)
    #part1
    print("part1:{}".format(find_marker(input_seq)))
    #PART2
    print("part2:{}".format(find_marker_part2(input_seq)))