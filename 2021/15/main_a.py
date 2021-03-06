import numpy as np

with open("data.txt") as f:
    input_data = f.read()

grid = np.array([list(x) for x in input_data.split("\n")], dtype=int)
shortest = np.zeros(grid.shape, dtype=int)
wall = 1000000
grid_len = len(grid)
i_max = 2 * grid_len - 1
for i in range(1, i_max):

    x_min = i - grid_len + 1 if i >= grid_len else 0
    x_max = grid_len - 1 if i >= grid_len else i

    for x in range(x_min, x_max + 1):

        y = i - x

        el_up = shortest[x - 1, y] if x != 0 else wall
        el_left = shortest[x, y - 1] if y != 0 else wall
        el_shortest = min([el_up, el_left]) + grid[x, y]

        # print(i,x,y,grid[x,y],el_up,el_left,el_shortest)

        shortest[x, y] = el_shortest

shortest[-1, -1]
