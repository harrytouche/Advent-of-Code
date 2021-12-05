with open("data.txt") as f:
    input_data = f.read()

parsed_data = input_data.split("\n")

breakout = [[0, 0] for x in range(len(parsed_data[0]))]


for i in range(len(parsed_data)):
    this_element = list(parsed_data[i])
    for j in range(len(this_element)):
        breakout[j][int(this_element[j])] += int(1)

print(breakout)

ga = [("0" if x[0] > x[1] else "1") for x in breakout]
ep = [("0" if x[0] < x[1] else "1") for x in breakout]

print(ga, ep)

ga = "".join(ga)
ep = "".join(ep)

print(ga, ep)

ga = int(ga, 2)
ep = int(ep, 2)

print(ga, ep, ga * ep)
