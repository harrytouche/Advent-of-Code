import numpy as np

with open("data.txt") as f:
    input_data = f.read()

parsed_data = [int(x) for x in input_data.split(",")]


# postion indexes
index_data = np.array([int(i) for i in range(max(parsed_data) + 1)])

# positions
position_data = np.zeros(max(parsed_data) + 1, dtype=int)
for n in parsed_data:
    position_data[n] += 1

best_i = False
best_sum = False
for i in range(len(position_data)):

    current_data = abs(index_data - i) * position_data
    current_data_sum = current_data.sum()

    print(i, current_data_sum)

    if not best_sum or current_data_sum < best_sum:
        best_sum = current_data_sum
        best_i = i

print("\n----Best----\n", best_i, best_sum)
