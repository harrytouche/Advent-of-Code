import regex as re

with open("data.txt") as f:
    input_data = f.read()


parsed_data = input_data.split("\n")

mapping = {
    "(": "a",
    ")": "b",
    "[": "c",
    "]": "d",
    "{": "e",
    "}": "f",
    "<": "g",
    ">": "h",
    "\n": "\n",
}


parsed_data = "".join([mapping[x] for x in input_data]).split("\n")

char_open = ["a", "c", "e", "g"]
char_closed = ["b", "d", "f", "h"]
match_string = "ab|cd|ef|gh"
finishes = []


def check_line_ok(line):

    output = True
    for n in range(len(line)):
        if line[n] in char_open:
            numbers = [0, 0, 0, 0]
            for m in range(n, len(line)):

                if line[m] in char_open:
                    numbers[char_open.index(line[m])] += 1

                if line[m] in char_closed:
                    numbers[char_closed.index(line[m])] -= 1

                check_issue = [True if x < 0 else False for x in numbers]
                if any(check_issue):
                    output = False
                    break

                check_finished = [True if x == 0 else False for x in numbers]
                if all(check_finished):
                    break
    return output


for line in parsed_data:

    if check_line_ok(line):
        running_line = line

        while running_line != re.sub(match_string, "", running_line):

            running_line = re.sub(match_string, "", running_line)

        this_finish = list(running_line)
        this_finish.reverse()
        finishes.append(this_finish)

scores = []
for finish in finishes:

    test = [char_open.index(x) + 1 for x in finish]

    score = 0
    for i in range(len(test)):
        score = (5 * score) + test[i]
    scores.append(score)

half = int((len(scores) - 1) / 2)
sorted(scores)[half : half + 1][0]
