import numpy as np

with open("data.txt") as f:
    input_data = f.read()

parsed_data = np.array([list(x) for x in input_data.split("\n")], dtype=int)


n_steps = 100
flashes = 0
running_data = parsed_data.copy()
for i in range(n_steps):

    # add one to each
    running_data += 1

    # check each element
    running_data_check = np.where(running_data > 9, True, False)

    while running_data_check.any():

        # add flashes
        flashes += len(running_data_check[running_data_check == True])

        # reset to -1 (goes to zero on next step)
        running_data = np.where(running_data_check == True, -1000, running_data)

        # add one to surrounding inc. diagonally
        for x in range(len(running_data)):
            for y in range(len(running_data[0])):

                if running_data_check[x, y] == True:

                    running_data[
                        max(0, x - 1) : min(x + 2, len(running_data)),
                        max(0, y - 1) : min(y + 2, len(running_data[0])),
                    ] += 1

        running_data_check = np.where(running_data > 9, True, False)

    # set negatives to 0
    running_data = np.where(running_data < 0, 0, running_data)
