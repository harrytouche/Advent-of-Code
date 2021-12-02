with open("data.txt") as f:
    input_data = f.read()

parsed_data = [(x.split(" ")[0], int(x.split(" ")[1])) for x in input_data.split("\n")]

x, y = 0, 0

for i in range(len(parsed_data)):

    this_element = parsed_data[i]

    if this_element[0] == "forward":
        x += this_element[1]

    if this_element[0] == "down":
        y += this_element[1]

    if this_element[0] == "up":
        y -= this_element[1]

print(x, y, x * y)
