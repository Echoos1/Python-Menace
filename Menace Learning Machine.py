flavor = 'RNG'  # Menace Training Type: Adversary, Human, RNG
trials = 1000000

if flavor == 'Adversary':
    from TrainingData import Adversary_DiMaggio_TTT_OMove as ost, \
        Adversary_DiMaggio_TTT_XMove as xst
elif flavor == 'Human':
    from TrainingData import Human_DiMaggio_TTT_OMove as ost, \
        Human_DiMaggio_TTT_XMove as xst
elif flavor == 'RNG':
    from TrainingData import RNG_DiMaggio_TTT_OMove as ost, \
        RNG_DiMaggio_TTT_XMove as xst
else:
    print("INVALID TRAINING FLAVOR")
    raise SystemError
import secrets
randgen = secrets.SystemRandom()


class Rewards:
    Menace1_Win = 2
    Menace1_Tie = 1
    Menace1_Lose = -1
    Menace2_Win = 2
    Menace2_Tie = 1
    Menace2_Lose = -1


class Game:
    OStateTable = ost.Dictionary.states
    XStateTable = xst.Dictionary.states
    XMoves = []
    OMoves = []
    board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    board_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    clear = '\n' * 100
    Xwins = 0
    Owins = 0
    Stalemates = 0

    @staticmethod
    def reset():
        Game.board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        Game.OMoves = []
        Game.XMoves = []

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
            return 'X Win'
        elif (board[0] == board[1] == board[2] and board[0] == 'O') or \
                (board[3] == board[4] == board[5] and board[3] == 'O') or \
                (board[6] == board[7] == board[8] and board[6] == 'O') or \
                (board[0] == board[3] == board[6] and board[0] == 'O') or \
                (board[1] == board[4] == board[7] and board[1] == 'O') or \
                (board[2] == board[5] == board[8] and board[2] == 'O') or \
                (board[0] == board[4] == board[8] and board[0] == 'O') or \
                (board[6] == board[4] == board[2] and board[6] == 'O'):
            return 'O Win'
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
    def read_board_X(state):
        state1 = f'{state[0]}{state[1]}{state[2]}{state[3]}{state[4]}{state[5]}{state[6]}{state[7]}{state[8]}'
        state2 = f'{state[2]}{state[5]}{state[8]}{state[1]}{state[4]}{state[7]}{state[0]}{state[3]}{state[6]}'
        state3 = f'{state[8]}{state[7]}{state[6]}{state[5]}{state[4]}{state[3]}{state[2]}{state[1]}{state[0]}'
        state4 = f'{state[6]}{state[3]}{state[0]}{state[7]}{state[4]}{state[1]}{state[8]}{state[5]}{state[2]}'

        if state1 in Game.OStateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.OStateTable[state1][0], Game.OStateTable[state1][1])
            index = Game.OStateTable[state1][0].index(choice[0])
            Game.OMoves.append([state1, index])
            templist[choice[0]] = "X"
            return choice[0]
        elif state2 in Game.OStateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.OStateTable[state2][0], Game.OStateTable[state2][1])
            index = Game.OStateTable[state2][0].index(choice[0])
            Game.OMoves.append([state2, index])
            templist[choice[0]] = "X"
            templist = [templist[6], templist[3], templist[0], templist[7], templist[4], templist[1], templist[8],
                        templist[5], templist[2]]
            choice = templist.index("X")
            return choice
        elif state3 in Game.OStateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.OStateTable[state3][0], Game.OStateTable[state3][1])
            index = Game.OStateTable[state3][0].index(choice[0])
            Game.OMoves.append([state3, index])
            templist[choice[0]] = "X"
            templist = [templist[8], templist[7], templist[6], templist[5], templist[4], templist[3], templist[2],
                        templist[1], templist[0]]
            choice = templist.index("X")
            return choice
        elif state4 in Game.OStateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.OStateTable[state4][0], Game.OStateTable[state4][1])
            index = Game.OStateTable[state4][0].index(choice[0])
            Game.OMoves.append([state4, index])
            templist[choice[0]] = "X"
            templist = [templist[2], templist[5], templist[8], templist[1], templist[4], templist[7], templist[0],
                        templist[3], templist[6]]
            choice = templist.index("X")
            return choice
        else:
            print("BOARD ERROR")
            raise SystemError

    @staticmethod
    def update_board_X(outcome, count):
        outcome = outcome
        count = count
        updated_table = Game.OStateTable

        if outcome == "Win" or outcome == "Stalemate":
            for i in Game.OMoves:
                updated_table[i[0]][1][i[1]] = updated_table[i[0]][1][i[1]]+count
        elif outcome == "Loss":
            for i in Game.OMoves:
                updated_table[i[0]][1][i[1]] = updated_table[i[0]][1][i[1]] + count
        Game.OStateTable = updated_table

    @staticmethod
    def write_board_X():
        if flavor == 'Adversary':
            with open("TrainingData/Adversary_DiMaggio_TTT_OMove.py", "w") as OMoveTable:
                OMoveTable.write('class Dictionary:\n')
                OMoveTable.write(f'\tstates = {Game.OStateTable}')
        elif flavor == 'Human':
            with open("TrainingData/Human_DiMaggio_TTT_OMove.py", "w") as OMoveTable:
                OMoveTable.write('class Dictionary:\n')
                OMoveTable.write(f'\tstates = {Game.OStateTable}')
        elif flavor == 'RNG':
            with open("TrainingData/RNG_DiMaggio_TTT_Medium.py", "w") as OMoveTable:
                OMoveTable.write('class Dictionary:\n')
                OMoveTable.write(f'\tstates = {Game.OStateTable}')

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

    @staticmethod
    def read_board_O(state):
        state1 = f'{state[0]}{state[1]}{state[2]}{state[3]}{state[4]}{state[5]}{state[6]}{state[7]}{state[8]}'
        state2 = f'{state[2]}{state[5]}{state[8]}{state[1]}{state[4]}{state[7]}{state[0]}{state[3]}{state[6]}'
        state3 = f'{state[8]}{state[7]}{state[6]}{state[5]}{state[4]}{state[3]}{state[2]}{state[1]}{state[0]}'
        state4 = f'{state[6]}{state[3]}{state[0]}{state[7]}{state[4]}{state[1]}{state[8]}{state[5]}{state[2]}'

        if state1 in Game.XStateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.XStateTable[state1][0], Game.XStateTable[state1][1])
            index = Game.XStateTable[state1][0].index(choice[0])
            Game.XMoves.append([state1, index])
            templist[choice[0]] = "O"
            return choice[0]
        elif state2 in Game.XStateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.XStateTable[state2][0], Game.XStateTable[state2][1])
            index = Game.XStateTable[state2][0].index(choice[0])
            Game.XMoves.append([state2, index])
            templist[choice[0]] = "O"
            templist = [templist[6], templist[3], templist[0], templist[7], templist[4], templist[1], templist[8],
                        templist[5], templist[2]]
            choice = templist.index("O")
            return choice
        elif state3 in Game.XStateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.XStateTable[state3][0], Game.XStateTable[state3][1])
            index = Game.XStateTable[state3][0].index(choice[0])
            Game.XMoves.append([state3, index])
            templist[choice[0]] = "O"
            templist = [templist[8], templist[7], templist[6], templist[5], templist[4], templist[3], templist[2],
                        templist[1], templist[0]]
            choice = templist.index("O")
            return choice
        elif state4 in Game.XStateTable:
            templist = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            r = secrets.SystemRandom()
            choice = r.choices(Game.XStateTable[state4][0], Game.XStateTable[state4][1])
            index = Game.XStateTable[state4][0].index(choice[0])
            Game.XMoves.append([state4, index])
            templist[choice[0]] = "O"
            templist = [templist[2], templist[5], templist[8], templist[1], templist[4], templist[7], templist[0],
                        templist[3], templist[6]]
            choice = templist.index("O")
            return choice
        else:
            print("BOARD ERROR")
            raise SystemError

    @staticmethod
    def update_board_O(outcome, count):
        outcome = outcome
        count = count
        updated_table = Game.XStateTable

        if outcome == "Win" or outcome == "Stalemate":
            for i in Game.XMoves:
                updated_table[i[0]][1][i[1]] = updated_table[i[0]][1][i[1]] + count
        elif outcome == "Loss":
            for i in Game.XMoves:
                updated_table[i[0]][1][i[1]] = updated_table[i[0]][1][i[1]] + count
        Game.XStateTable = updated_table

    @staticmethod
    def write_board_O():
        if flavor == 'Adversary':
            with open("TrainingData/Adversary_DiMaggio_TTT_XMove.py", "w") as XMoveTable:
                XMoveTable.write('class Dictionary:\n')
                XMoveTable.write(f'\tstates = {Game.XStateTable}')
        elif flavor == 'Human':
            with open("TrainingData/Human_DiMaggio_TTT_XMove.py", "w") as XMoveTable:
                XMoveTable.write('class Dictionary:\n')
                XMoveTable.write(f'\tstates = {Game.XStateTable}')
        elif flavor == 'RNG':
            with open("TrainingData/RNG_DiMaggio_TTT_XMove.py", "w") as XMoveTable:
                XMoveTable.write('class Dictionary:\n')
                XMoveTable.write(f'\tstates = {Game.XStateTable}')


def X_turn():
    Game.board[Game.read_board_X(Game.board)] = 'X'


def Y_turn():
    if flavor == 'Adversary':
        Game.board[Game.read_board_O(Game.board)] = 'O'
    elif flavor == 'Human':
        Game.show_board()
        r = input("Your Move ")
        try:
            int(r)
        except ValueError:
            print("Please input an integer index of an open space... ")
            Y_turn()
        r = int(r)
        if Game.board[r] != '_':
            print("That space is taken, please choose another...")
            Y_turn()
        elif r > 8:
            print("Invalid Index, please choose another... ")
            Y_turn()
        else:
            Game.board[r] = 'O'
    elif flavor == 'RNG':
        r = randgen.choice(Game.board_spaces)
        Game.board[r] = 'O'


def play():
    Game.reset()
    while True:
        outcome = ''
        Game.board_index()
        X_turn()
        if Game.check_board() == 'X Win':
            outcome = 'X Win'
            break
        elif Game.check_board() == 'Stalemate':
            outcome = 'Stalemate'
            break
        Game.board_index()
        Y_turn()
        if Game.check_board() == 'O Win':
            outcome = 'O Win'
            break
        elif Game.check_board() == 'Stalemate':
            outcome = 'Stalemate'
            break

    if outcome == "X Win":
        Game.Xwins += 1
        Game.update_board_X("Win", Rewards.Menace1_Win)
        Game.update_board_O("Loss", Rewards.Menace2_Lose)
    elif outcome == "Stalemate":
        Game.Stalemates += 1
        Game.update_board_X("Stalemate", Rewards.Menace1_Tie)
        Game.update_board_O("Stalemate", Rewards.Menace2_Tie)
    elif outcome == "O Win":
        Game.Owins += 1
        Game.update_board_X("Loss", Rewards.Menace1_Lose)
        Game.update_board_O("Win", Rewards.Menace2_Win)
    else:
        print("OUTCOME ERROR")
        raise SystemError

    #print(outcome)


print(f'Training Mode: {flavor}\n'
      f'Rewards:\n'
      f'\tWin: {Rewards.Menace1_Win}\n'
      f'\tTie: {Rewards.Menace1_Tie}\n'
      f'\tLose: {Rewards.Menace1_Lose}')

if flavor == 'Adversary':
    print(f'Trials: {trials}')
    for i in range(trials):
        play()
elif flavor == 'Human':
    while True:
        play()
        Game.write_board_X()
        Game.write_board_O()
        replay = input("Play Again? (y/n) ")
        if replay.lower() in ['y', 'yes', 'yeah', 'sure', 'heck, why not?', 'absolutely']:
            print('\n\n\n')
            pass
        else:
            break
elif flavor == 'RNG':
    print(f'Trials: {trials}')
    for i in range(trials):
        play()


print(Game.OStateTable)
print(Game.XStateTable)
print(f'\n'
      f'X Wins {Game.Xwins} - ({round((Game.Xwins / trials) * 100, 3)}%)\n'
      f'O Wins {Game.Owins} - ({round((Game.Owins / trials) * 100, 3)}%)\n'
      f'Stalemates {Game.Stalemates} - ({round((Game.Stalemates / trials) * 100, 3)}%)')
fin = input("Update Master Table? (y/n) ")
if fin == "y":
    Game.write_board_X()
    Game.write_board_O()
else:
    pass
