filename = "C:\\Users\\wcorr\\Desktop\\Advent of Code\\day 5\\data.txt"
with open(filename) as f:
    translation = {66: 49, 70: 48, 76: 48, 82:49}
    content = f.readlines()

    content = [int(item.translate(translation).strip(), 2) for item in content]

print(max(content))

