import re

def remove_newline(map):
    for i in range(len(map)):
        map[i] = map[i].replace("\n", "")


def extendmap(map, duplicate):
    for i, row in enumerate(map):
        map[i] = map[i] * duplicate

def navigate(map, right, down):
    tree = 0
    col = 0
    for row in range(down, len(map), down):
        col += right
        string = map[row]
        if string[col] == '#':
            tree += 1
    return tree
        

if __name__ == '__main__':
    map = [line for line in open("input_files/puzzle3_input.txt", "r").readlines()]
    char_per_row = map[0].__len__()
    rows = map.__len__()
    remove_newline(map)
    map1 = map[:]
    duplicate = rows * 3 + 1 # problem statement one down three right
    extendmap(map1, duplicate)
    # part 1
    tree1 = navigate(map1, 3, 1)
    print("number of trees is:", tree1)
    #part 2
    map2 = map[:]
    duplicate = rows * 1 + 1 # problem statement one down three right
    extendmap(map2, duplicate)
    tree2 = navigate(map2, 1, 1)
    print("number of trees is:", tree2)

    map3 = map[:]
    duplicate = rows * 5 + 1 # problem statement one down three right
    extendmap(map3, duplicate)
    tree3 = navigate(map3, 5, 1)
    print("number of trees is:", tree3)

    map4 = map[:]
    duplicate = rows * 7 + 1 # problem statement one down three right
    extendmap(map4, duplicate)
    tree4 = navigate(map4, 7, 1)
    print("number of trees is:", tree4)

    map5 = map[:]
    duplicate = rows * 1 + 2 # problem statement one down three right
    extendmap(map5, duplicate)
    tree5 = navigate(map5, 1, 2)
    print("number of trees is:", tree5)
    #multiplier:
    print("part2 ans after multiplication:", tree1*tree2*tree3*tree4*tree5)
