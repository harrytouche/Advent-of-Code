import regex as re
import numpy as np


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
            
def v_x_0_min():
    for i in range(x_min):
        x_sum = 0
        for x in range(i,0,-1):
            x_sum += x
        if x_sum >= x_min:
            break
    return i
    
            
n_success=0

v_x_min = v_x_0_min()
v_x_max = x_max+1
v_y_min = min(y_max,y_min)
v_y_max = 1000

print(v_x_min,v_x_max,v_y_min,v_y_max)

for i in range(v_x_min,v_x_max):
    print(i)
    for j in range(v_y_min,v_y_max):
    
        v = np.array([i,j], dtype=int)
        d = np.array([0,0], dtype=int)
        h_max = 0
        success = False
        for k in range(1000):
            
            d += v
            
            v[0] = v[0]-1 if v[0]>0 else 0
            v[1] -= 1
            
            
            if is_in_target(d):
                #print("In target! {}".format(d))
                success = True
                break
            
            elif is_past_target(d):
                #print("Past target! {}".format(d))
                break
        
        if success == True:
            n_success += 1
        #print(success,h_max,i)
        
print("\n\n",n_success)