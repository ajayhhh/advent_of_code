def process_input(input):
    for i in range(len(input)):
        input[i] = input[i].rstrip()
        
def how_many_fully_contained(input):
    '''how_many_fully_contained'''
    #part 1
    overlap_count = 0
    for item in input:
        x, y = item.split(',')
        x1, y1 = x.split('-')
        x2, y2 = y.split('-')
        if x2 >= x1 <= y1 and y2 <= y1 >= x1:
            overlap_count += 1
        elif x1 >= x2 <= y2 and y1 <= y2 >= x2:
            overlap_count += 1
    return overlap_count
    

def how_many_partially_contained(input):
    ''' how_many_partially_contained'''
    count = 0
    for item in input:
        x, y = item.split(',')
        x1, y1 = x.split('-')
        x2, y2 = y.split('-')
        # using negative condition: check if pairs do not overlap
        if int(y1)<int(x2) or int(y2)<int(x1):
            count+=1
    return len(input) - count # remaining ones does overlap partially/fully
    

if __name__ == '__main__':
    input_list = [line for line in open("C:\Work\\advent_of_code\\2022\input_files\puzzle4_input.txt", "r").readlines()]
    process_input(input_list)
    #part1
    print("part1:{}".format(how_many_fully_contained(input_list)))
    #PART2
    print("part2:{}".format(how_many_partially_contained(input_list)))