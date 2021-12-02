def increase_check(input):
    increased = 0
    for idx in range(len(input)):
        if idx >= 1:
            if input[idx] > input[idx - 1]:
                increased += 1
    return increased

def increase_check_triplets(input):
    increased = 0
    for idx in range(len(input)):
        if idx >= 3:
            if (input[idx] + input[idx - 1] + input[idx - 2]) > \
               (input[idx - 1] + input[idx - 2] + input[idx - 3]):
                    increased += 1
    return increased

if __name__ == '__main__':
    input_list = [int(line) for line in open("input_files/puzzle1_input.txt", "r").readlines()]
    #part1
    print(increase_check(input_list))
    #PART2
    print(increase_check_triplets(input_list))