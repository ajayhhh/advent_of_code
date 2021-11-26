import re

def checkpasswords1(pwd_rule_items):
    count = 0
    for item in pwd_rule_items:
        low, high, must_have, pw = re.split('-| |: ', item)
        character_count = pw.count(must_have)
        if (int(low) <= character_count <= int(high)):
            count += 1
    return count

def checkpasswords2(pwd_rule_items):
    count = 0
    for item in pwd_rule_items:
        low, high, must_have, pw = re.split('-| |: ', item)
        if (pw[int(low)-1] == must_have and pw[int(high)-1] != must_have) or (pw[int(low)-1] != must_have and pw[int(high)-1] == must_have):
            count += 1
    return count


if __name__ == '__main__':
    pwd_rule_items = [line for line in open("input_files/puzzle2_input.txt", "r").readlines()]
    #part1
    print(checkpasswords1(pwd_rule_items))
    #part2
    print(checkpasswords2(pwd_rule_items))