with open("data.txt") as f:
    input_data = f.read()

parsed_data = input_data.split("\n")


# largest
running_data = parsed_data
for j in range(len(parsed_data[0])):

    n_0, n_1 = 0, 0

    for i in range(len(running_data)):

        this_element = list(running_data[i])

        if this_element[j] == "0":
            n_0 += 1
        else:
            n_1 += 1

    digit = "1" if n_1 >= n_0 else "0"
    running_data = [x for x in running_data if x[j] == digit]

ox = int(running_data[0], 2)


# smallest
running_data = parsed_data
for j in range(len(parsed_data[0])):

    n_0, n_1 = 0, 0

    for i in range(len(running_data)):

        this_element = list(running_data[i])

        if this_element[j] == "0":
            n_0 += 1
        else:
            n_1 += 1

    digit = "0" if n_0 <= n_1 else "1"
    running_data = [x for x in running_data if x[j] == digit]
    if len(running_data) == 1:
        break

co = int(running_data[0], 2)

print(ox, co, ox * co)
