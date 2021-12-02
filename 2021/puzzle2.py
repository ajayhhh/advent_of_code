def process_input(input):
    direction = []
    count = []
    for idx in range(len(input)):
        dir, cnt = input[idx].split(" ")
        direction.append(dir), count.append(int(cnt))
    return zip(direction, count)

def navigate_and_multiply(input):
    #part 1 x, y
    x = 0
    y = 0
    #part 2 aim, aim_depth
    aim = 0
    aim_depth = 0
    for dir, cnt in input:
        if dir == "forward":
            x += cnt
            aim_depth += (aim * cnt)
        elif dir == "down":
            y += cnt
            aim += cnt
        elif dir == "up":
            y -= cnt
            aim -= cnt
        else:
            pass
    return x * y , x * aim_depth

if __name__ == '__main__':
    input_list = [line for line in open("input_files/puzzle2_input.txt", "r").readlines()]
    processed_input = process_input(input_list)
    #part1
    part1 , part2 = navigate_and_multiply(processed_input)
    print(part1)
    #PART2
    print(part2)