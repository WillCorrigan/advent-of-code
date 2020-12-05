filename = "C:\\Users\\wcorr\\Desktop\\Advent of Code\\day 5\\data.txt"
with open(filename) as f:
    translation = {66: 49, 70: 48, 76: 48, 82:49}
    content = f.readlines()

    content = [int(item.translate(translation).strip(), 2) for item in content]
    content = sorted(content)

    def find_missing(lst):
        return [x for x in range(lst[0], lst[-1]+1) if x not in lst]

    print(find_missing(content))