# Part 1

def read_input():
    with open('input') as f:
        lines = f.read().splitlines()
        return lines


def find_gamma_epsilon(data):
    gamma = ''
    epsilon = ''
    half = len(data) / 2

    for i in range(len(data[0])):
        count_0 = 0
        count_1 = 0
        for entry in data:
            if entry[i] == '0':
                count_0 += 1
                if count_0 >= half:
                    gamma += '0'
                    epsilon += '1'
                    break

            else:
                count_1 += 1
                if count_1 >= half:
                    gamma += '1'
                    epsilon += '0'
                    break

    return int(gamma, 2), int(epsilon, 2)


# Part 2

def most_common_bits(data, position):

    has_0_in_position = []
    has_1_in_position = []

    for entry in data:
        if entry[position] == '0':
            has_0_in_position.append(entry)
        else:
            has_1_in_position.append(entry)

    if len(has_0_in_position) > len(has_1_in_position):
        if len(has_0_in_position) > 1:
            return most_common_bits(has_0_in_position, position + 1)
        elif len(has_0_in_position) == 1:
            return has_0_in_position
        else:
            return most_common_bits(data, position + 1)
    else:
        if len(has_1_in_position) > 1:
            return most_common_bits(has_1_in_position, position + 1)
        elif len(has_1_in_position) == 1:
            return has_1_in_position
        else:
            return most_common_bits(data, position + 1)


def least_common_bits(data, position):

    has_0_in_position = []
    has_1_in_position = []

    for entry in data:
        if entry[position] == '0':
            has_0_in_position.append(entry)
        else:
            has_1_in_position.append(entry)

    if len(has_0_in_position) > len(has_1_in_position):
        if len(has_1_in_position) > 1:
            return least_common_bits(has_1_in_position, position + 1)
        elif len(has_1_in_position) == 1:
            return least_common_bits
        else:
            return least_common_bits(data, position + 1)
    else:
        if len(has_0_in_position) > 1:
            return least_common_bits(has_0_in_position, position + 1)
        elif len(has_0_in_position) == 1:
            return has_0_in_position
        else:
            return least_common_bits(data, position + 1)


data = read_input()
testcase = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
testis = ['01', '00']

gamma, epsilon = find_gamma_epsilon(testcase)
print(f'Part 1: {gamma} * {epsilon} = {gamma * epsilon}')

oxygen = int(most_common_bits(data, 0)[0], 2)
co2 = int(least_common_bits(data, 0)[0], 2)
print(f'Part 2: {oxygen} * {co2} = {oxygen * co2}')
