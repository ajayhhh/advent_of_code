def process_input(input):
    for i in range(len(input)):
        input[i] = input[i].rstrip()
        
def func1(input):
    '''Func1'''
    #part 1 power consumption
    

def func2(input):
    ''' Func2'''
    

if __name__ == '__main__':
    input_list = [line for line in open("input_files/puzzlex_input.txt", "r").readlines()]
    process_input(input_list)
    #part1
    print(func1(input_list))
    #PART2
    print(func2(input_list))