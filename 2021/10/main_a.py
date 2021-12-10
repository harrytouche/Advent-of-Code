from time import sleep
import numpy as np

with open("data.txt") as f:
    input_data = f.read()

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
char_values = [3, 57, 1197, 25137]

bad_chars = []


for line in parsed_data:

    bad_char = False
    print(line)

    for n in range(len(line)):

        # print("\n",n,"\n")

        if line[n] in char_open:

            numbers = [0, 0, 0, 0]

            for m in range(n, len(line)):

                if line[m] in char_open:
                    # print("add one")
                    numbers[char_open.index(line[m])] += 1

                if line[m] in char_closed:
                    # print("take one")
                    numbers[char_closed.index(line[m])] -= 1

                check_issue = [True if x < 0 else False for x in numbers]
                # print(check_issue)
                if any(check_issue):
                    # print("ISSUE!")
                    # print(numbers, n, m)
                    bad_char = char_closed[check_issue.index(True)]
                    print(bad_char)
                    break

                check_finished = [True if x == 0 else False for x in numbers]
                # print(check_finished)
                if all(check_finished):
                    # print("This one is ok")
                    # print(numbers, n, m)
                    break

        else:
            print("not an open")

        if bad_char is not False:
            print("Found bad char: {}".format(bad_char))
            bad_chars.append(bad_char)
            break


print(bad_chars)
print(np.array([char_values[char_closed.index(x)] for x in bad_chars]).sum())
#        sleep(5)


# take 1st element

# look along line

# if see same element add one

# if see other element, take 1

# if see other element and =0,
