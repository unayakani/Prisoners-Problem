import random

file = open("result.txt", "a")

n_prisoners = 500

for _ in range(200):
    boxes = [x for x in range(1, n_prisoners + 1)]
    slips = boxes.copy()
    random.shuffle(slips)

    boxes_with_slips = dict(zip(boxes, slips))

    successes = list()

    for i in range(1, n_prisoners + 1):
        _buffer = i

        for j in range(1, int((n_prisoners + 1) / 2)):
            _buffer = boxes_with_slips[_buffer]
            if _buffer == i:
                break

        if _buffer != i:
            successes.append("Failed")
        else:
            successes.append("Passed")

    if "Failed" in successes:
        file.write("Executed\n")
    else:
        file.write("Pardoned\n")

n_executed = 0
n_pardoned = 0

with open('result.txt') as result:
    for line in result:
        if line == "Executed\n":
            n_executed += 1
        elif line == "Pardoned\n":
            n_pardoned += 1

percentage_pardoned = ( n_pardoned / (n_pardoned + n_executed) ) * 100

print("Pardoned percentage is: ", percentage_pardoned, "%")
