import numpy as np

with open("data.txt") as f:
    input_data = f.read()

parsed_data = np.array([list(x) for x in input_data.split("\n")], dtype=int)
parsed_data = np.pad(
    parsed_data,
    (1, 1),
    "constant",
    constant_values=(parsed_data.max() + 1, parsed_data.max() + 1),
)

risk = 0

for i in range(1, len(parsed_data) - 1):
    for j in range(1, len(parsed_data[0]) - 1):

        tests = [
            parsed_data[i, j] < parsed_data[i, j - 1],
            parsed_data[i, j] < parsed_data[i, j + 1],
            parsed_data[i, j] < parsed_data[i - 1, j],
            parsed_data[i, j] < parsed_data[i + 1, j],
        ]

        if all(tests):
            # print("\n\n{},{}\n".format(i,j),parsed_data[i-1:i+2,j-1:j+2],"\n")
            risk += parsed_data[i, j] + 1

print(risk)
