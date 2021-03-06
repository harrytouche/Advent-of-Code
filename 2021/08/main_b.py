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
n with 5 = 3 (2, 3, 5)
n with 6 = 3 (0, 6, 9)
n with 7 = 1
"""
import numpy as np

with open("data.txt") as f:
    input_data = f.read()

parsed_data = input_data.split("\n")
prepped_data = []

for data in parsed_data:
    this_line = data.split(" | ")
    prepped_data.append([this_line[0].split(" "), this_line[1].split(" ")])

running_list = []
for line in prepped_data:

    input_n = [[False, x] for x in line[0]]
    output_n = line[1]

    i, i_max = 0, 10
    while i < i_max and len([x for x in input_n if x[0] is False]) > 0:

        for remaining in [x for x in input_n if x[0] is False]:

            if len(remaining[1]) == 2:
                remaining[0] = "1"

            elif len(remaining[1]) == 3:
                remaining[0] = "7"

            elif len(remaining[1]) == 4:
                remaining[0] = "4"

            elif len(remaining[1]) == 7:
                remaining[0] = "8"

            # already found the 1, 4, 7, 8 digits
            elif len([x for x in input_n if x[0] is not False]) >= 4:

                # if 6 digits and does not contain the 4 digits then 9
                if len(remaining[1]) == 6:

                    # if 6 digits and DOES contain the 4 digits then 9
                    if all(
                        x in remaining[1]
                        for x in list([x for x in input_n if x[0] == "4"][0][1])
                    ):
                        remaining[0] = "9"

                    # if 6 digits and does not contain the 1 digits then 6
                    elif not all(
                        x in remaining[1]
                        for x in list([x for x in input_n if x[0] == "1"][0][1])
                    ):
                        remaining[0] = "6"

                    # if 6 digits and last one then 0
                    elif (
                        len([x for x in input_n if x[0] is False and len(x[1]) == 6])
                        == 1
                    ):
                        remaining[0] = "0"

                # already found all the above
                elif len([x for x in input_n if x[0] is not False]) >= 7:
                    # if 5 digits and DOES contain the 1 digits then 3
                    if len(remaining[1]) == 5:

                        # if 5 digits and DOES contain the 1 digits then 3
                        if all(
                            [
                                x in remaining[1]
                                for x in list([x for x in input_n if x[0] == "1"][0][1])
                            ]
                        ):
                            remaining[0] = "3"

                        elif all(
                            [
                                x in list([x for x in input_n if x[0] == "9"][0][1])
                                for x in list(remaining[1])
                            ]
                        ):
                            remaining[0] = "5"

                        else:
                            remaining[0] = "2"

        i += 1

    # sort the numbers in both arrays
    input_n = [[x[0], "".join(sorted(x[1]))] for x in input_n]
    output_list = []
    for digit in output_n:
        digit = "".join(sorted(digit))
        for test in input_n:
            test[1] = "".join(sorted(test[1]))
            if test[1] == digit:
                output_list.append(test[0])

    running_list.append("".join(output_list))

    # extract the four digits

    # sum and add to running total

print(running_list)

print(np.array(running_list, dtype=int).sum())
