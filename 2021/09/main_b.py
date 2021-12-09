import numpy as np

with open("data.txt") as f:
    input_data = f.read()

parsed_data = np.array([list(x) for x in input_data.split("\n")], dtype=int)


from scipy.ndimage import measurements

parsed_data = np.where(parsed_data < parsed_data.max(), 1, 0)
a, b = measurements.label(parsed_data)

tot_up = sorted([a[a == x].size for x in range(1, a.max() + 1)])
print(tot_up[-3:], np.array(tot_up[-3:]).prod())
