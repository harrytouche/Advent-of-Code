import regex as re
import numpy as np
from tqdm import tqdm

with open("data.txt") as f:
    input_data = f.read()
    
x_min,x_max,y_min,y_max = [int(x) for x in re.match("target area: x=(.+)\.\.(.+), y=(.+)\.\.(.+)",input_data)[1:]]


def is_in_target(d):
    x,y = d
    return True if (
        min(x_min,x_max) <= x <= max(x_min,x_max)) and (
        min(y_min,y_max) <= y <= max(y_min,y_max)
    ) else False
        
            
def is_past_target(d):
    x,y = d
    return True if (
        x > max(x_min,x_max)) or (
        y < min(y_min,y_max)
    ) else False
            
            
h_max_max = 0

for i in tqdm(range(100)):
    for j in range(1000):
    
        v = np.array([i,j], dtype=int)
        d = np.array([0,0], dtype=int)
        h_max = 0
        success = False
        for k in range(10000):
            
            d += v
            
            v[0] = v[0]-1 if v[0]>0 else 0
            v[1] -= 1
            
            h_max = max(h_max,d[1])
            
            if is_in_target(d):
                #print("In target! {}".format(d))
                success = True
                break
            
            elif is_past_target(d):
                #print("Past target! {}".format(d))
                break
        
        if success == True:
            h_max_max = max(h_max,h_max_max)
        #print(success,h_max,i)
        
print(h_max_max)