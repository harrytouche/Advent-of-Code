import regex as re
import numpy as np

with open("data.txt") as f:
    input_data = f.read()

initial_dots = [x.split(",") for x in input_data.split("\n\n")[0].split("\n")]
max_x, max_y = np.array(initial_dots, dtype=int).max(axis=0)


match_string = "fold along ([xy]{1})=([0-9]+)$"
folds = [
    [re.match(match_string, x)[1], int(re.match(match_string, x)[2])]
    for x in input_data.split("\n\n")[1].split("\n")
]

grid = np.zeros((max_y + 1, max_x + 1), dtype=int)

for dot_x, dot_y in initial_dots:
    grid[int(dot_y), int(dot_x)] += 1


max_n = len(folds)

for i in range(max_n):

    # print(i)
    # print(len(grid),len(grid[0]))
    direction, number = folds[i]
    print("d,n = {},{}".format(direction, number))

    if direction == "y":

        if len(grid) % 2 != 0:
            grid = np.delete(grid, int(len(grid) / 2), axis=0)

        sec_a, sec_b = np.split(grid, 2, axis=0)

        """
        sep = len(grid)%2
        sec_a = grid[:number,:]
        sec_b = grid[number+sep:,:]
        """

        sec_b = np.flip(sec_b, axis=0)

    elif direction == "x":

        if len(grid[0]) % 2 != 0:
            grid = np.delete(grid, int(len(grid[0]) / 2), axis=1)

        sec_a, sec_b = np.split(grid, 2, axis=1)

        """
        sep = len(grid[0])%2
        sec_a = grid[:,:number]
        sec_b = grid[:,number+sep:]
        """

        sec_b = np.flip(sec_b, axis=1)

    grid = sec_a + sec_b
    grid = np.where(grid > 0, 1, 0)
