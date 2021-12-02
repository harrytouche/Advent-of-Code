with open("input.txt") as f:
    input_data = f.read()

parsed_data = [int(x) for x in input_data.split("\n")]

output_data = 0

for i in range(1, len(parsed_data)):
    if parsed_data[i] > parsed_data[i - 1]:
        output_data += 1

print(output_data)
