filename = "C:\\Users\\wcorr\\Desktop\\Advent of Code\\day 2\\data.txt"
with open(filename) as f:
    content = f.readlines()

content = [line.strip().split(": ") for line in content]

correct_passwords = 0
for arr, password in content:
    amount = arr[0:-2].split("-")
    letter = "".join(arr[-1].split("-"))
    pw = password
    first_index = pw[int(amount[0])-1]
    second_index = pw[int(amount[1])-1]


    if first_index != second_index and (first_index == letter or second_index == letter) :
        correct_passwords += 1




print(correct_passwords)