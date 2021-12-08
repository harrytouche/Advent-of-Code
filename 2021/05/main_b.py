import numpy as np

with open("data.txt") as f:
    input_data = f.read()

parsed_data = input_data.split("\n")
parsed_data = [
    [[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in parsed_data
]


grid = np.zeros((1000, 1000), dtype=int)


for line in parsed_data:

    y_1 = line[0][0]
    x_1 = line[0][1]
    y_2 = line[1][0]
    x_2 = line[1][1]

    # print(x_1,y_1,x_2,y_2)
    # grid[x_1:x_2+1,y_1:y_2+1] += 1

    x_modifier = 1 if x_2 >= x_1 else -1
    y_modifier = 1 if y_2 >= y_1 else -1

    if x_1 == x_2 or y_1 == y_2:

        for x in range(x_1, x_2 + x_modifier, x_modifier):
            for y in range(y_1, y_2 + y_modifier, y_modifier):
                # print(x, y)
                grid[x, y] += 1

    else:
        x, y = x_1, y_1
        while x != x_2 and y != y_2:

            # print(x,y,x_1,y_1,x_2,y_2)

            grid[x, y] += 1

            x += x_modifier
            y += y_modifier

            # extra one at the end if needed
            if x == x_2 and y == y_2:
                grid[x, y] += 1
                break


print((grid >= 2).sum())
