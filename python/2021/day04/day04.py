# Part 1

def read_input():
    with open('input') as f:
        lines = f.read().splitlines()
        return lines

def prepare_boards(data):
    numbers_drawn = data.pop(0).split(',')
    data.pop(0)
    boards = []
    board = []
    marked = []
    zero_board = []
    for d in data:
        if d != '':
            line = d.replace('  ', ' 0')
            if line.startswith(' '):
                line = '0'+line[1:]
            board.append(line)
            zero_board.append([0,0,0,0,0])
        else:
            boards.append(board)
            board = []
            marked.append(zero_board)
            zero_board = []
    boards.append(board)
    marked.append(zero_board)
    return numbers_drawn, boards, marked


def play_bingo_first(numbers_drawn, boards, marked):
    for n in numbers_drawn:
        if len(n) == 1:
            n = '0'+n
        for i in range(len(boards)):
            for j in range(5):
                #for k in range(len(boards[0])-1):
                k = boards[i][j].find(n)
                if k > -1:
                    marked[i][j][int(k/3)] = 1
                    #print(marked[i])
                    if marked[i][j].count(1) == 5 or list(map(list, zip(*marked[i])))[j].count(1) == 5:
                        print('bingo!')
                        return calculate_score(boards[i], marked[i], int(n))
                    break
    return 'No winners :('


def calculate_score(board, marked, n):
    sum = 0
    for i in range(5):
        for j in range(5):
            if marked[i][j] == 0:
                sum += int(board[i][j*3:(j*3)+2])
    return sum*n


data = read_input()
numbers, boards, marked = prepare_boards(data)
print(boards)
print(f'Part 1: {play_bingo_first(numbers, boards, marked)}')

