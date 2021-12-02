# Part 1

def read_input():
    with open('input') as f:
        lines = f.readlines()
        return lines


def calculate_final_position(lines):
    horizontal = 0
    depth = 0
    for l in lines:
        split = l.split(' ')
        direction = split[0]
        value = int(split[1])
        if 'forward' in direction:
            horizontal += value
        else:
            depth = depth + value if 'down' in direction else depth - value
    return horizontal, depth


# testcase = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
horizontal, depth = calculate_final_position(read_input())
print('Part 1: {} * {} = {}'.format(horizontal, depth, horizontal * depth))


# Part 2

def calculate_final_position_with_aim(lines):
    horizontal = 0
    depth = 0
    aim = 0
    for l in lines:
        split = l.split(' ')
        direction = split[0]
        value = int(split[1])
        if 'forward' in direction:
            horizontal += value
            depth += aim*value
        else:
            aim = aim + value if 'down' in direction else aim - value

    return horizontal, depth


horizontal, depth = calculate_final_position_with_aim(read_input())
print('Part 2: {} * {} = {}'.format(horizontal, depth, horizontal * depth))
