import copy

with open("data.txt") as f:
    input_data = f.read()


transitions = {}
for x in input_data.split("\n\n")[1].split("\n"):
    transitions[x.split(" -> ")[0]] = [x.split(" -> ")[1], 0]
transitions_blank = copy.deepcopy(transitions)

template = input_data.split("\n\n")[0]
for x in range(len(template) - 1):
    transitions[template[x : x + 2]][1] += 1


x, x_max = 0, 40
while x < x_max:

    print(x, x_max)
    # print(transitions_blank)
    new_transitions = copy.deepcopy(transitions_blank)
    # print(new_transitions)

    for key in transitions.keys():

        if transitions[key][1] > 0:
            # print(new_transitions)

            new_key_list = list(key)
            new_key_list.insert(1, transitions[key][0])

            new_key_a = "".join(new_key_list[:-1])
            new_key_b = "".join(new_key_list[1:])
            print(key, new_key_a, new_key_b)

            new_transitions[new_key_a][1] += transitions[key][1]
            new_transitions[new_key_b][1] += transitions[key][1]

    transitions = copy.deepcopy(new_transitions)

    x += 1


unique = dict.fromkeys(list("".join(transitions.keys())), 0)

for key in transitions.keys():

    for i in list(key):

        unique[i] += transitions[key][1]


max_n = int(max(unique.values()))
min_n = int(min(unique.values()))

# could have missed out the ends, but was fine


print("\n", max_n, min_n, (max_n - min_n) / 2)
