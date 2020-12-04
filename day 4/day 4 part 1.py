import re

filename = "C:\\Users\\wcorr\\Desktop\\Advent of Code\\day 4\\data.txt"
with open(filename) as f:
    content = f.read()

pattern = '\n\n'
split_by_pattern = re.split(pattern, content)
list_of_passports = [item.replace('\n', " ").split() for item in split_by_pattern]


total = 0
valid_terms = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

for passport in list_of_passports:
    compare_terms = ([elem.split(':')[0] for elem in passport])
    result = all(elem in compare_terms for elem in valid_terms)
    if result:
        total+=1



print(total)