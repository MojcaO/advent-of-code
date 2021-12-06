# Part 1

def read_input():
    with open('input') as f:
        lines = f.read().split(',')
        return list(map(int, lines))


def lanternfish_population(data, days):
    for i in range(days):
        ready = data.count(0)
        data = [6 if x==0 else x-1 for x in data]
        for j in range(ready):
            data.append(8)

    return len(data)


# Part 2

def lanternfish_overflow(data, days):
    age_counters = []
    for age in range(9):
        age_counters.append(data.count(age))

    for i in range(days):
        ready = age_counters.pop(0)
        age_counters.append(ready)
        age_counters[6] += ready

    return sum(age_counters)


data = read_input()
testcase = [3,4,3,1,2]
print(f'Part 1: There are {lanternfish_population(data, 80)} lanternfish after 80 days.')
print(f'Part 2: There are {lanternfish_overflow(data, 256)} lanternfish after 256 days.')



