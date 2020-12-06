filename = "C:\\Users\\wcorr\\Desktop\\Advent of Code\\day 6\\data.txt"
with open(filename) as f:
   content = f.read().split("\n\n")
   content = [elem.split("\n") for elem in content]
   content = sum([len(set(list(''.join(x)))) for x in content])

print(content)