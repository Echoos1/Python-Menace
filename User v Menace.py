flavor = 'RNG'  # Menace Training Type: Adversary, Human, RNG

if flavor == 'Adversary':
    from TrainingData import Adversary_DiMaggio_TTT_OMove as ost
elif flavor == 'Human':
    from TrainingData import Human_DiMaggio_TTT_OMove as ost
elif flavor == 'RNG':
    from TrainingData import RNG_DiMaggio_TTT_OMove as ost
import secrets
randgen = secrets.SystemRandom()


class Game:
    StateTable = ost.Dictionary.states
    Moves = []
    board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    board_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    clear = '\n' * 100

    @staticmethod
    def reset():
        Game.board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        Game.Moves = []

    @staticmethod
    def check_board():
        board = Game.board
        if (board[0] == board[1] == board[2] and board[0] == 'X') or \
                (board[3] == board[4] == board[5] and board[3] == 'X') or \
                (board[6] == board[7] == board[8] and board[6] == 'X') or \
                (board[0] == board[3] == board[6] and board[0] == 'X') or \
                (board[1] == board[4] == board[7] and board[1] == 'X') or \
                (board[2] == board[5] == board[8] and board[2] == 'X') or \
                (board[0] == board[4] == board[8] and board[0] == 'X') or \
                (board[6] == board[4] == board[2] and board[6] == 'X'):
            return 'Win'
        elif (board[0] == board[1] == board[2] and board[0] == 'O') or \
                (board[3] == board[4] == board[5] and board[3] == 'O') or \
                (board[6] == board[7] == board[8] and board[6] == 'O') or \
                (board[0] == board[3] == board[6] and board[0] == 'O') or \
                (board[1] == board[4] == board[7] and board[1] == 'O') or \
                (board[2] == board[5] == board[8] and board[2] == 'O') or \
                (board[0] == board[4] == board[8] and board[0] == 'O') or \
                (board[6] == board[4] == board[2] and board[6] == 'O'):
            return 'Loss'
        elif '_' not in Game.board:
            return 'Stalemate'
        else:
            return 'Continue'

    @staticmethod
    def board_index():
        Game.board_spaces = []
        for i in range(9):
            if Game.board[i] == '_':
                Game.board_spaces.append(i)

    @staticmethod
    def read_board(state):
        state1 = f'{state[0]}{state[1]}{state[2]}{state[3]}{state[4]}{state[5]}{state[6]}{state[7]}{state[8]}'
        state2 = f'{state[2]}{state[5]}{state[8]}{state[1]}{state[4]}{state[7]}{state[0]}{state[3]}{state[6]}'
        state3 = f'{state[8]}{state[7]}{state[6]}{state[5]}{state[4]}{state[3]}{state[2]}{state[1]}{state[0]}'
        state4 = f'{state[6]}{state[3]}{state[0]}{state[7]}{state[4]}{state[1]}{state[8]}{state[5]}{state[2]}'

        if state1 in Game.StateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.StateTable[state1][0], Game.StateTable[state1][1])
            index = Game.StateTable[state1][0].index(choice[0])
            Game.Moves.append([state1, index])
            templist[choice[0]] = "X"
            return choice[0]
        elif state2 in Game.StateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.StateTable[state2][0], Game.StateTable[state2][1])
            index = Game.StateTable[state2][0].index(choice[0])
            Game.Moves.append([state2, index])
            templist[choice[0]] = "X"
            templist = [templist[6], templist[3], templist[0], templist[7], templist[4], templist[1], templist[8],
                        templist[5], templist[2]]
            choice = templist.index("X")
            return choice
        elif state3 in Game.StateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.StateTable[state3][0], Game.StateTable[state3][1])
            index = Game.StateTable[state3][0].index(choice[0])
            Game.Moves.append([state3, index])
            templist[choice[0]] = "X"
            templist = [templist[8], templist[7], templist[6], templist[5], templist[4], templist[3], templist[2],
                        templist[1], templist[0]]
            choice = templist.index("X")
            return choice
        elif state4 in Game.StateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.StateTable[state4][0], Game.StateTable[state4][1])
            index = Game.StateTable[state4][0].index(choice[0])
            Game.Moves.append([state4, index])
            templist[choice[0]] = "X"
            templist = [templist[2], templist[5], templist[8], templist[1], templist[4], templist[7], templist[0],
                        templist[3], templist[6]]
            choice = templist.index("X")
            return choice
        else:
            print("BOARD ERROR")
            raise SystemError

    @staticmethod
    def show_board():
        show = Game.board[:]
        for s in range(9):
            if show[s] == '_':
                show[s] = ' '
        print(f'{Game.clear}'
              f'   █   █   \n'
              f' {show[0]} █ {show[1]} █ {show[2]} \n'
              f'   █   █   \n'
              f'███████████\n'
              f'   █   █   \n'
              f' {show[3]} █ {show[4]} █ {show[5]} \n'
              f'   █   █   \n'
              f'███████████\n'
              f'   █   █   \n'
              f' {show[6]} █ {show[7]} █ {show[8]} \n'
              f'   █   █   ')


def X_turn():
    Game.board[Game.read_board(Game.board)] = 'X'


def Y_turn():
    Game.show_board()
    r = int(input("Your Move "))
    if Game.board[r] != '_':
        print("That space is taken, please choose another...")
        Y_turn()
    elif r > 8:
        print("Invalid Index, please choose another... ")
        Y_turn()
    else:
        Game.board[r] = 'O'

def play():
    Game.reset()
    while True:
        outcome = ''
        Game.board_index()
        X_turn()
        if Game.check_board() == 'Win':
            outcome = 'Win'
            break
        elif Game.check_board() == 'Stalemate':
            outcome = 'Stalemate'
            break
        Game.board_index()
        Y_turn()
        if Game.check_board() == 'Loss':
            outcome = 'Loss'
            break
        elif Game.check_board() == 'Stalemate':
            outcome = 'Stalemate'
            break

    Game.show_board()
    if outcome == "Win":
        print("Menace Wins")
    elif outcome == "Stalemate":
        print("Stalemate")
    elif outcome == "Loss":
        print("You Win!")
    else:
        print("OUTCOME ERROR")
        raise SystemError

    replay = input("Play Again? (y/n) ")
    if replay.lower() in ['y', 'yes', 'yeah', 'sure', 'heck, why not?', 'absolutely']:
        print('\n\n\n')
        play()

play()
