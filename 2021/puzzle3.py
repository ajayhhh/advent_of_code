def remove_new_line_char(input):
    for i in range(len(input)):
        input[i] = input[i].rstrip()
        
def diagnose(input):
    #part 1 power consumption
    bit_count_zero = [0] * len(input[0])
    bit_count_one = [0] * len(input[0])
    for item in input:
        #count number of bits in each of the positions of a single element
        for idx, bit in enumerate(item):
            if bit == '0':
                bit_count_zero[idx] += 1
            elif bit == '1':
                bit_count_one[idx] += 1
            else:
                print("Ooops!!, unknown input or unhandled exception occured. Answer may not be correct")
    gamma_rate = ''
    epsilon_rate = ''
    #problem logic to calculate gamma rate and epsilon rate
    for i in range(len(bit_count_zero)):
        if bit_count_zero[i] > bit_count_one[i]:
            gamma_rate = gamma_rate + str(1)
            epsilon_rate = epsilon_rate + str(0)
        else:
            gamma_rate = gamma_rate + str(0)
            epsilon_rate = epsilon_rate + str(1)
    #convert binary to decimal
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    #return the product which is the answer to part 1
    return gamma_rate * epsilon_rate

def short_list(input, iterate, key):
    num_zeroes = 0
    num_ones = 0
    temp0 = []
    temp1 = []
    short_list = []
    if len(input) == 1:
        return input
    for item in input:
        if item[iterate] == '0':
            num_zeroes += 1
            temp0.append(item)
            continue
        elif item[iterate] == '1':
            num_ones += 1
            temp1.append(item)
            continue
        else:
            print("Unhandled exception. Answer may not be correct!!")
    if key == 1:
        if (num_zeroes > num_ones):
            short_list = temp0
        elif (num_ones > num_zeroes):
            short_list = temp1
        elif num_zeroes == num_ones:
            short_list = temp1
    elif key == 0:
        if num_zeroes > num_ones:
            short_list = temp1
        elif num_zeroes == num_ones:
            short_list = temp0
        else:
            short_list = temp0
    return short_list

def diagnose2(input):
    ''' To calculate oxygen generator rating and 
    CO2 scrubber rating'''
    iterate = 0
    o2_gen_rating = []
    co2_scrub_rating = []
    #iterate through the input list for max the length of the input
    while(iterate < len(input[0])):
        num_zeroes = 0
        num_ones = 0
        temp0 = []
        temp1 = []
        #first iteration needs full input
        if iterate == 0:
            o2_gen_rating = short_list(input, iterate, 1)
            co2_scrub_rating = short_list(input, iterate, 0)
            iterate += 1
            continue
        #successive iteration needs reduced/short-listed input
        #To short-list items, send short-list from previous iteraion,
        #current iteration and a key (1 or o2 and 0 for co2)
        # key was determined from the problem statement
        o2_gen_rating = short_list(o2_gen_rating, iterate, 1)
        co2_scrub_rating = short_list(co2_scrub_rating, iterate, 0)
        iterate += 1
    o2 = o2_gen_rating[0]
    co2 = co2_scrub_rating[0]
    o2_gen_rating = int(o2, 2)
    co2_scrub_rating = int(co2, 2)
    return o2_gen_rating * co2_scrub_rating

if __name__ == '__main__':
    input_list = [line for line in open("input_files/puzzle3_input.txt", "r").readlines()]
    remove_new_line_char(input_list)
    #part1
    print(diagnose(input_list))
    #PART2
    print(diagnose2(input_list))