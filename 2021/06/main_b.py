import numpy as np

with open("data.txt") as f:
    input_data = f.read()
    
parsed_data = [int(x) for x in input_data.split(",")]


n_days = 256

initial_fish = np.zeros(9, dtype=float)
for n in parsed_data:
    initial_fish[n] += 1

running_fish = initial_fish

for i in range(n_days):
    
    # get zeroes
    breeding_fish = initial_fish[0]
    
    # shuffle down
    initial_fish[:-1] = initial_fish[1:]
    
    # reset last fish
    initial_fish[-1] = 0
    
    # reset existing 0 to 6 and add new 8
    initial_fish[6] += breeding_fish
    initial_fish[8] += breeding_fish
    
    
    
    
print(initial_fish)
print(initial_fish.sum())
