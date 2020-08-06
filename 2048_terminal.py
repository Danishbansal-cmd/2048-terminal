import random

#variable
SCORE = 0

def board():
    board =  [['   .','   .','   .','   .'],['   .','   .','   .','   .'],['   .','   .','   .','   .'],
              ['   .','   .','   .','   .']]
    return board

def draw_board(board):
    for x in range(4):
        for y in range(4):
            print('{}|'.format(board[x][y]), end = " ")
        print()
    print('SCORE-BOARD = ',SCORE)
    print('press -1 to move left          press -2 to move right')
    print('press -3 to move up          press -4 to move down')

def add_random(board):
    list = []
    for x in range(4):
        for y in range(4):
            if board[x][y] == '   .':
                list.append([x,y])
    r = round(random.random() * 100)
    number = 0
    if r < 80:
        number = 2
    else:
        number = 4
    x = random.choice(list)
    lth = 4 - len(str(number))
    board[x[0]][x[1]] = " " * lth + str(number)


board = board()
add_random(board)
add_random(board)
input1 = 0


run = True
other = True
while run:
    draw_board(board)
    if other:
        for x in range(4):
            for y in range(4):
                if board[x][y] == '2048':
                    print('Do you want to continue the game :\n'
                          'press -1 to continue')
                    input2 = int(input('Enter the number: '))
                    if input2 == 1:
                        run = True
                        other = False
                    else:
                        run = False

                        break
    input1 = int(input("write the number: "))
    print('your input: ', input1)
    if input1 == 1:
        value = False
        for i in range(3):
            for x in range(4):
                for y in range(1,4):
                    if board[x][y] != '   .':
                        if board[x][y - 1] == '   .':
                            board[x][y - 1] = board[x][y]
                            board[x][y] = '   .'
                            value = True
        for x in range(4):
            for y in range(1, 4):
                if board[x][y] == board[x][y - 1] and board[x][y] != '   .':
                    result = int(board[x][y]) + int(board[x][y - 1])
                    SCORE += result
                    lth = 4 - len(str(result))
                    board[x][y - 1] = " "*lth + str(result)
                    board[x][y] = '   .'
                    value = True
        for x in range(4):
            for y in range(1, 4):
                if board[x][y] != '   .':
                    if board[x][y - 1] == '   .':
                        board[x][y - 1] = board[x][y]
                        board[x][y] = '   .'
        print(value,'LEFT')
        if value:
            add_random(board)
    elif input1 == 2:
        value = False
        for i in range(3):
            for x in range(4):
                for y in range(2,-1,-1):
                    if board[x][y] != '   .':
                        if board[x][y + 1] == '   .':
                            board[x][y + 1] = board[x][y]
                            board[x][y] = '   .'
                            value = True
        for x in range(4):
            for y in range(2, -1, -1):
                if board[x][y] == board[x][y + 1] and board[x][y] != '   .':
                    result = int(board[x][y]) + int(board[x][y + 1])
                    SCORE += result
                    lth = 4 - len(str(result))
                    board[x][y + 1] = " " * lth + str(result)
                    board[x][y] = '   .'
                    value = True
        for x in range(4):
            for y in range(2,-1,-1):
                if board[x][y] != '   .':
                    if board[x][y + 1] == '   .':
                        board[x][y + 1] = board[x][y]
                        board[x][y] = '   .'
        print(value,'RIGHT')
        if value:
            add_random(board)

    elif input1 == 3:
        value = False
        for i in range(3):
            for x in range(1,4):
                for y in range(4):
                    if board[x][y] != '   .':
                        if board[x - 1][y] == '   .':
                            board[x - 1][y] = board[x][y]
                            board[x][y] = '   .'
                            value = True
        for x in range(1, 4):
            for y in range(4):
                if board[x][y] == board[x - 1][y] and board[x][y] != '   .':
                    result = int(board[x][y]) + int(board[x - 1][y])
                    SCORE += result
                    lth = 4 - len(str(result))
                    board[x - 1][y] = " " * lth + str(result)
                    board[x][y] = '   .'
                    value = True
        for x in range(1, 4):
            for y in range(4):
                if board[x][y] != '   .':
                    if board[x - 1][y] == '   .':
                        board[x - 1][y] = board[x][y]
                        board[x][y] = '   .'
        print(value,'UP')
        if value:
            add_random(board)
    elif input1 == 4:
        value = False
        for i in range(3):
            for x in range(2,-1,-1):
                for y in range(4):
                    if board[x][y] != '   .1':
                        if board[x + 1][y] == '   .':
                            board[x + 1][y] = board[x][y]
                            board[x][y] = '   .'
                            value = True
        for x in range(2, -1, -1):
            for y in range(4):
                if board[x][y] == board[x + 1][y] and board[x][y] != '   .':
                    result = int(board[x][y]) + int(board[x + 1][y])
                    SCORE += result
                    lth = 4 - len(str(result))
                    board[x + 1][y] = " " * lth + str(result)
                    board[x][y] = '   .'
                    value = True
        for x in range(2, -1, -1):
            for y in range(4):
                if board[x][y] != '   .1':
                    if board[x + 1][y] == '   .':
                        board[x + 1][y] = board[x][y]
                        board[x][y] = '   .'
        print(value,'DOWN')
        if value:
            add_random(board)
