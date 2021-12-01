# Part 1

def read_ints(file):
    with open(file) as f:
        lines = f.readlines()
        return set(map(int, lines))


def find_sum(numbers, sum):
    for a in numbers:
        b = sum - a
        if b in numbers:
            return a, b
    raise TypeError('Sum ' + str(sum) + ' not found.')


report = read_ints('input')
a, b = find_sum(report, 2020)
print('{} * {} = {}'.format(a, b, a*b))


# Part 2

def find_sum_of_three(numbers, sum):
    while numbers:
        x = numbers.pop()
        newsum = sum - x
        try:
            y, z = find_sum(numbers, newsum)
            return x, y, z
        except TypeError:
            continue


x,y,z = find_sum_of_three(report, 2020)
print('{} * {} * {} = {}'.format(x, y, z, x*y*z))

