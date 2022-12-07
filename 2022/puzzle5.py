def process_input(input):
    for i in range(len(input)):
        input[i] = input[i].rstrip()

instruction_line_number = 0
total_stacks = 0
#        [J]         [B]     [T]    
#        [M] [L]     [Q] [L] [R]    
#        [G] [Q]     [W] [S] [B] [L]
#[D]     [D] [T]     [M] [G] [V] [P]
#[T]     [N] [N] [N] [D] [J] [G] [N]
#[W] [H] [H] [S] [C] [N] [R] [W] [D]
#[N] [P] [P] [W] [H] [H] [B] [N] [G]
#[L] [C] [W] [C] [P] [T] [M] [Z] [W]
# 1   2   3   4   5   6   7   8   9 
stack1 = ['L', 'N', 'W', 'T', 'D']
stack2 = ['C', 'P', 'H']
stack3 = ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J',]
stack4 = ['C', 'W', 'S', 'N', 'T', 'Q', 'L']
stack5 = ['P', 'H', 'C', 'N']
stack6 = ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B']
stack7 = ['M', 'B', 'R', 'J', 'G', 'S', 'L']
stack8 = ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T']
stack9 = ['W', 'G', 'D', 'N', 'P', 'L']

stack_1 = ['L', 'N', 'W', 'T', 'D']
stack_2 = ['C', 'P', 'H']
stack_3 = ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J',]
stack_4 = ['C', 'W', 'S', 'N', 'T', 'Q', 'L']
stack_5 = ['P', 'H', 'C', 'N']
stack_6 = ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B']
stack_7 = ['M', 'B', 'R', 'J', 'G', 'S', 'L']
stack_8 = ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T']
stack_9 = ['W', 'G', 'D', 'N', 'P', 'L']

def convert_input_to_list(input):
    ''' convert_input_to_list'''
    input_container_line_num = 0
    global instruction_line_number
    global total_stacks
    for idx, row in enumerate(input):
        if ']' in row:
            continue
        else:
            total_stacks = row.split(' ')[-1]
            instruction_line_number = idx + 2
            input_container_line_num = idx
            break    

temp_buf = "" # used to return top most container of each stack
old_size = 0 # old size of destination container used for reversing the order

def rearrange_crates(input):
    '''rearrange_crates'''
    #part 1
    global instruction_line_number
    global total_stacks
    for idx in range(instruction_line_number, len(input)):
        #get move instruction
        _, num_of_containers, _, src, _, dest = input[idx].split(' ')
        # Ex: ['move', '6', 'from', '6', 'to', '5']
        for num in range(1,int(num_of_containers)+1):  # +1 as list index starts from 0
            exec("stack{0}.append(stack{1}.pop(-1))".format(dest, src))
    ret_string = ""
    global temp_buf # used to return top most container of each stack
    global stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9
    for i in range(1, int(total_stacks)+1):
        exec("temp_buf = stack{0}[-1]".format(i), globals()) 
        ret_string = ret_string + temp_buf 
    return ret_string
        

def rearrange_crates_part2(input):
    ''' part2'''
    global instruction_line_number
    global total_stacks
    for idx in range(instruction_line_number, len(input)):
        #get move instruction
        _, num_of_containers, _, src, _, dest = input[idx].split(' ')
        # Ex: ['move', '6', 'from', '6', 'to', '5']
        movable_items = []
        exec("old_size=len(stack_{0})".format(dest), globals())
        for num in range(1,int(num_of_containers)+1):  # +1 as list index starts from 0
            exec("stack_{0}.append(stack_{1}.pop(-1))".format(dest, src))
        # a[2:]=reversed(a[2:]) this reverses from 3rd element until end of list
        exec("stack_{0}[{1}:]=reversed(stack_{0}[{1}:])".format(dest, int(old_size)))
    ret_string = ""
    global temp_buf # used to return top most container of each stack
    global stack_1,stack_2,stack_3,stack_4,stack_5,stack_6,stack_7,stack_8,stack_9
    for i in range(1, int(total_stacks)+1):
        exec("temp_buf = stack_{0}[-1]".format(i), globals()) 
        ret_string = ret_string + temp_buf
    return ret_string
    

if __name__ == '__main__':
    input_list = [line for line in open("C:\Work\\advent_of_code\\2022\input_files\puzzle5_input.txt", "r").readlines()]
    process_input(input_list)
    convert_input_to_list(input_list)
    #part1
    print("part1:{}".format(rearrange_crates(input_list)))
    #PART2
    print("part2:{}".format(rearrange_crates_part2(input_list)))