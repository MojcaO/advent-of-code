# Part 1

def read_measurements():
    with open('input') as f:
        lines = f.readlines()
        lines = [int(i) for i in lines]
        return lines


def count_increases(measurements):
    counter = 0
    for i in range(len(measurements) - 1):
        if measurements[i] < measurements[i + 1]:
            counter += 1
    return counter


testcase = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
measurements = read_measurements()
print('Part 1: '+str(count_increases(measurements)))


# Part 2

def count_increases_sliding_sums(measurements):
    counter = 0
    previous = sum(measurements[:3])

    for i in range(1, len(measurements) - 2):
        current = sum(measurements[i:i+3])
        if current > previous:
            counter += 1
        previous = current
    return counter


print('Part 2: '+str(count_increases_sliding_sums(measurements)))
