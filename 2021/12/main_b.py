f = open("data.txt", "r")
x = f.read()
data = [line.split("-") for line in x.splitlines()]
data += [pair[::-1] for pair in data]

incomplete = [["start"]]
complete = []

while len(incomplete) > 0:
    processing = incomplete.pop(0)
    for current, target in data:
        if current != processing[-1]:
            continue
        if target.upper() != target and target in processing:
            continue
        newPath = [processing + [target]]
        if target == "end":
            complete += newPath
        else:
            incomplete += newPath

print(len(complete))

incomplete = [[["start"], ""]]
complete = []

while len(incomplete) > 0:
    processing, twice = incomplete.pop(0)
    for current, target in data:
        if current != processing[-1]:
            continue
        if target == "start" or (
            target.upper() != target and target in processing and twice != ""
        ):
            continue
        newPath = [
            [
                processing + [target],
                [twice, target][target.upper() != target and target in processing],
            ]
        ]
        if target == "end":
            complete += newPath
        else:
            incomplete += newPath

print(len(complete))
