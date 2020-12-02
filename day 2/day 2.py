import re

filename = "C:\\Users\\wcorr\\Desktop\\Advent of Code\\day 2\\data.txt"
with open(filename) as f:
    content = f.readlines()

content = [line.strip().split(": ") for line in content]

correct_passwords = 0;
for arr, password in content:
    amount = arr[0:-2].split("-")
    letter = "".join(arr[-1].split("-"))
    pw = password
    min_amount = int(amount[0])
    max_amount = int(amount[1])

    if pw.count(letter) >= min_amount and pw.count(letter) <= max_amount:
        correct_passwords += 1



print(correct_passwords)