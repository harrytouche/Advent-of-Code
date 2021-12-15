with open("data.txt") as f:
    input_data = f.read()

template = input_data.split("\n\n")[0]
transitions_prep = input_data.split("\n\n")[1].split("\n")
transitions = {}
for x in transitions_prep:

    transitions[x.split(" -> ")[0]] = x.split(" -> ")[1]

x, x_max = 0, 10
while x < x_max:

    new_template = ""
    for i in range(len(template) - 1):
        new_template += template[i] + transitions[template[i : i + 2]]

        if i == len(template) - 2:
            new_template += template[-1]

    template = new_template
    x += 1


split = list(template)
unique = dict.fromkeys(split, 0)

for x in split:
    unique[x] += 1

max_n = max(unique.values())
min_n = min(unique.values())

print(max_n, min_n, max_n - min_n)
