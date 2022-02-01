import secrets
randgen = secrets.SystemRandom()


class Game():
    board_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]


board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
board_print = f'{board[0]}{board[1]}{board[2]}\n{board[3]}{board[4]}{board[5]}\n{board[6]}{board[7]}{board[8]}'

def check_win():
    if (board[0] == board[1] == board[2] and board[0] == 'X') or \
             (board[3] == board[4] == board[5] and board[3] == 'X') or \
             (board[6] == board[7] == board[8] and board[6] == 'X') or \
             (board[0] == board[3] == board[6] and board[0] == 'X') or \
             (board[1] == board[4] == board[7] and board[1] == 'X') or \
             (board[2] == board[5] == board[8] and board[2] == 'X') or \
             (board[0] == board[4] == board[8] and board[0] == 'X') or \
             (board[6] == board[4] == board[2] and board[6] == 'X'):
        return 'X'
    elif (board[0] == board[1] == board[2] and board[0] == 'O') or \
             (board[3] == board[4] == board[5] and board[3] == 'O') or \
             (board[6] == board[7] == board[8] and board[6] == 'O') or \
             (board[0] == board[3] == board[6] and board[0] == 'O') or \
             (board[1] == board[4] == board[7] and board[1] == 'O') or \
             (board[2] == board[5] == board[8] and board[2] == 'O') or \
             (board[0] == board[4] == board[8] and board[0] == 'O') or \
             (board[6] == board[4] == board[2] and board[6] == 'O'):
        return 'O'
    elif '_' not in board:
        return 'S'
    else:
        return 'n'


def X_turn():
    r = randgen.choice(Game.board_spaces)
    board[r] = 'X'


def Y_turn():
    r = randgen.choice(Game.board_spaces)
    board[r] = 'O'

def index():
    Game.board_spaces = []
    for i in range(9):
        if board[i] == '_':
            Game.board_spaces.append(i)

while True:
    index()
    X_turn()
    if check_win() == 'X':
        print('X Wins')
        break
    elif check_win() == 'S':
        print("Stalemate")
        break
    index()
    Y_turn()
    if check_win() == 'O':
        print('O Wins')
        break
    elif check_win() == 'S':
        print("Stalemate")
        break

board_print = f'{board[0]}{board[1]}{board[2]}\n{board[3]}{board[4]}{board[5]}\n{board[6]}{board[7]}{board[8]}'
print(f'\n{board_print}')