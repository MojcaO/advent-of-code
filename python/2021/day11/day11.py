# Part 1

def read_input():
    with open('input') as f:
        input = f.readlines()
        grid = []

        for i in input:
            line = i.split()
            line = [int(l) for l in line[0]]
            grid.append(line)
        return grid


def next_step(grid):
    flashes = 0
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1
            if grid[i][j] == 10:
                grid, f = flash(grid, i, j)
                flashes += f

    for i in range(10):
        for j in range(10):
            if grid[i][j] > 9:
                grid[i][j] = 0

    return grid, flashes


def flash(grid, i, j):
    flashes = 1
    for ii in range(i-1, i+2):
        if 0 <= ii < 10:
            for jj in range(j-1, j+2):
                if 0 <= jj < 10:
                    grid[ii][jj] += 1
                    if grid[ii][jj] == 10:
                        grid, f = flash(grid, ii, jj)
                        flashes += f
    return grid, flashes


grid = read_input()
steps = 1000
total_flashes = 0
for i in range(1,steps+1):
    grid, flashes = next_step(grid)
    total_flashes += flashes
    if flashes == 100:
        print(f'Octopus synchronization reached at step {i}!')
        break
print(f'After {i} steps there have been a total of {total_flashes} flashes.')


