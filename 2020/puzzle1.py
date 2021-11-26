def iterate(input_list):
    for i in range(len(input_list)):
        if i < (len(input_list) - 1):
            for j in range((i+1), len(input_list)):
                #part 1
                #if (input_list[i] + input_list[j]) == 2020:
                    #return (input_list[i] * input_list[j])
                #part 2
                if j < (len(input_list) - 2):
                    for k in range ((j+1), len(input_list)):
                        if (input_list[i] + input_list[j] + input_list[k]) == 2020:
                            return (input_list[i] * input_list[j] * input_list[k])

if __name__ == '__main__':
    input_list = [int(line) for line in open("input_files/puzzle1_input.txt", "r").readlines()]
    print(iterate(input_list))