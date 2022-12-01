def process_input(input):
    for i in range(len(input)):
        input[i] = input[i].rstrip()
        
def find_elf_with_max_calories(input):
    '''find_elf_with_max_energy'''
    #part 1 find elf with max calories
    elves = [0]
    elf_index = 0
    for calorie in input:
        if calorie is not '':
            elves[elf_index] += int(calorie)
        elif calorie is '':
            elf_index += 1
            elves.append(0)
        else:
            print("Unhandled exception occured")
    return max(elves)

def find_total_highest3(input):
    '''find_total_highest3'''
    #part 2 total of top 3 energetic elves
    elves = [0]
    elf_index = 0
    for calorie in input:
        if calorie is not '':
            elves[elf_index] += int(calorie)
        elif calorie is '':
            elf_index += 1
            elves.append(0)
        else:
            print("Unhandled exception occured")
    elves.sort(reverse=True)
    return elves[0] + elves[1] + elves[2] 
    

if __name__ == '__main__':
    input_list = [line for line in open("C:\Work\\advent_of_code\\2022\input_files\puzzle1_input.txt", "r").readlines()]
    process_input(input_list)
    #part1
    print("Highest calories carried by any elf is: {}".format(find_elf_with_max_calories(input_list)))
    #part2
    print("Total calories carried by elves with top 3 highest calories is: {}".format(find_total_highest3(input_list)))