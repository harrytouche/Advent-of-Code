# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 10:41:00 2021

@author: harry
"""

with open("data.txt") as f:
    input_data = f.read()
parsed_data = input_data.split("\n\n")

# get called out numbers
called_numbers = parsed_data[0].split(",")

# create transposed list of grids as well
grids_a = [[y.split() for y in x.split("\n")] for x in parsed_data[1:]]
grids_b = []
for grid in grids_a:
    grids_b.append(list(map(list, zip(*grid))))


def check_grid_for_complete(input_grid_list):

    output = False
    for i in range(len(input_grid_list)):
        for line in input_grid_list[i]:
            if len(line) == 0:
                output = i

        if output != False:
            break

    return output


for i in range(len(called_numbers)):
    for grid in grids_a:
        for line in grid:
            if called_numbers[i] in line:
                line.remove(called_numbers[i])

    for grid in grids_b:
        for line in grid:
            if called_numbers[i] in line:
                line.remove(called_numbers[i])

    grid_a_complete = check_grid_for_complete(grids_a)
    grid_b_complete = check_grid_for_complete(grids_b)
    if grid_a_complete or grid_b_complete:
        break


# get specific complete grid
if grid_a_complete:
    complete_grid = grids_a[grid_a_complete]

elif grid_b_complete:
    complete_grid = grids_b[grid_b_complete]

remaining_numbers = [int(x) for y in complete_grid for x in y]

output = sum(remaining_numbers) * int(called_numbers[i])

print(output)
