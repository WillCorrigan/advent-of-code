filename = "C:\\Users\\wcorr\\Desktop\\Advent of Code\\data.txt"
with open(filename) as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

print(content)



for x in content:
    storedvarx = x
    for y in content:
        storedvary = y
        for z in content:
            if x + y + z == 2020:
                print(x*y*z)