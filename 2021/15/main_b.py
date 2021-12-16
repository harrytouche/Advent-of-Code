import numpy as np

with open("data.txt") as f:
    input_data = f.read()

grid = np.array([list(x) for x in input_data.split("\n")], dtype=int)
new_size = (len(grid) * 5, len(grid[0]) * 5)
new_grid = np.zeros((new_size), dtype=int)

for i in range(5):
    for j in range(5):
        x_min = i * len(grid)
        y_min = j * len(grid)
        new_grid[x_min : x_min + len(grid), y_min : y_min + len(grid)] = grid + i + j

new_grid = np.where(new_grid > 9, new_grid - 9, new_grid)
grid = new_grid

shortest = np.zeros(new_size, dtype=int)
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
