import numpy as np

with open("small.txt") as f:
    input_data = f.read()

grid = np.array([list(x) for x in input_data.split("\n")], dtype=int)

