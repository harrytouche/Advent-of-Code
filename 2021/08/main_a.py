with open("data.txt") as f:
    input_data = f.read()

parsed_data = input_data.split("\n")
prepped_data = []

for data in parsed_data:
    this_line = data.split(" | ")
    prepped_data.append([this_line[0].split(" "), this_line[1].split(" ")])


def check_numbers(input_string):
    if len(input_string) == 2:
        return "1"

    elif len(input_string) == 3:
        return "7"

    elif len(input_string) == 4:
        return "4"

    elif len(input_string) == 7:
        return "8"

    else:
        return False


counter = 0
for line in prepped_data:
    for entry in line[1]:
        if check_numbers(entry) is not False:
            counter += 1

print(counter)

"""
number -> n lines
0 -> 6
1 -> 2
2 -> 5
3 -> 5
4 -> 4
5 -> 5
6 -> 6
7 -> 3
8 -> 7
9 -> 6

n with 1 = 0
n with 2 = 1
n with 3 = 1
n with 4 = 1
n with 5 = 3
n with 6 = 3
n with 7 = 1
"""
