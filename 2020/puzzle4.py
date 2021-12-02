import re

class Passport:
    def __init__(self, birthyear, issueyear, expiration, height, haircol, eyecol, pid, cid = None):
        self.birthyear = birthyear
        self.issueyear = issueyear
        self.expiration = expiration
        self.height = height
        self.haircol = haircol
        self.eyecol = eyecol
        self.pid = pid
        self.cid = cid
    
    def validate_pp(self):
        pass


if __name__ == '__main__':
    file_content = [line for line in open("input_files/puzzle4_input.txt", "r").readlines()]
    for line in file_content:
        


#sample data
#pid:371817422 ecl:blu byr:1964
#iyr:2018
#eyr:2021 cid:176
#hgt:153cm hcl:#888785