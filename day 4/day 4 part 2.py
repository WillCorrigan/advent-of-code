import re

filename = "C:\\Users\\wcorr\\Desktop\\Advent of Code\\day 4\\data.txt"
with open(filename) as f:
    content = f.read()

pattern = '\n\n'
split_by_pattern = re.split(pattern, content)
list_of_passports = [item.replace('\n', " ").split() for item in split_by_pattern]



def ValidCheck(dictionary):
    if 1920 <= int(dictionary['byr']) <= 2002\
            and 2010 <= int(dictionary['iyr']) <= 2020\
            and 2020 <= int(dictionary['eyr']) <= 2030\
            and re.match(r'\d+..', dictionary['hgt'])\
            and (dictionary['hgt'].endswith('cm') and 150 <= int(dictionary['hgt'][:-2]) <= 193 or dictionary['hgt'].endswith('in') and 59 <= int(dictionary['hgt'][:-2]) <= 76)\
            and re.match(r'^#[\da-f]{6}$', dictionary['hcl'])\
            and dictionary['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']\
            and re.match(r'^\d{9}$', dictionary['pid']):
            return True
    

total = 0
valid_terms = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

for passport in list_of_passports:
    dictionary_passports = {key: value for key, value in (elem.split(':') for elem in passport)}
    result = all(elem in dictionary_passports.keys() for elem in valid_terms)
    if result:
        if ValidCheck(dictionary_passports):
            total +=1




print(total)