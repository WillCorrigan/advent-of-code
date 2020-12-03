filename = "C:\\Users\\wcorr\\Desktop\\Advent of Code\\day 3\\data.txt"
with open(filename) as f:
    content = f.readlines()

split_routes = [coord.strip() for coord in content]

number_of_trees = 0
x_coord = 0
y_coord = 0

while y_coord < len(split_routes):
    if x_coord >= len(split_routes[0]):
        x_coord -= len(split_routes[0])
    if split_routes[y_coord][x_coord] == "#":
        number_of_trees += 1
        print(f"tree at {x_coord+1}, {y_coord+1}")
    x_coord += 3
    y_coord += 1

print(number_of_trees)