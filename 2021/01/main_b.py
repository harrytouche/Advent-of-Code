with open("input.txt") as f:
    input_data = f.read()

parsed_data = [int(x) for x in input_data.split("\n")]

output_data = 0

for i in range(1, len(parsed_data) - 2):
    window_now = parsed_data[i] + parsed_data[i + 1] + parsed_data[i + 2]
    window_previous = parsed_data[i - 1] + parsed_data[i] + parsed_data[i + 1]

    if window_now > window_previous:
        output_data += 1


print(output_data)
