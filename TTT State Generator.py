board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
iters = []
iter1 = []
iter2 = []
iter3 = []
iter4 = []
iter5 = []
iter6 = []
iter7 = []
iter8 = []
iter9 = []
O_Moves = {}
X_Moves = {}


def check(state):
    state = state
    if ([state[0], state[1], state[2], state[3], state[4], state[5], state[6], state[7], state[8]] in iters) or \
            ([state[2], state[5], state[8], state[1], state[4], state[7], state[0], state[3], state[6]] in iters) or \
            ([state[8], state[7], state[6], state[5], state[4], state[3], state[2], state[1], state[0]] in iters) or \
            ([state[6], state[3], state[0], state[7], state[4], state[1], state[8], state[5], state[2]] in iters):
        #print("Duplicate")
        return 'Stop'
    elif (state[0] == state[1] == state[2] and state[0] == 'X') or \
            (state[3] == state[4] == state[5] and state[3] == 'X') or \
            (state[6] == state[7] == state[8] and state[6] == 'X') or \
            (state[0] == state[3] == state[6] and state[0] == 'X') or \
            (state[1] == state[4] == state[7] and state[1] == 'X') or \
            (state[2] == state[5] == state[8] and state[2] == 'X') or \
            (state[0] == state[4] == state[8] and state[0] == 'X') or \
            (state[6] == state[4] == state[2] and state[6] == 'X'):
       #print("X WIN")
        return 'Win'
    elif (state[0] == state[1] == state[2] and state[0] == 'O') or \
            (state[3] == state[4] == state[5] and state[3] == 'O') or \
            (state[6] == state[7] == state[8] and state[6] == 'O') or \
            (state[0] == state[3] == state[6] and state[0] == 'O') or \
            (state[1] == state[4] == state[7] and state[1] == 'O') or \
            (state[2] == state[5] == state[8] and state[2] == 'O') or \
            (state[0] == state[4] == state[8] and state[0] == 'O') or \
            (state[6] == state[4] == state[2] and state[6] == 'O'):
        #print("O WIN")
        return 'Win'


# Initial Board State
O_Moves[f'{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}{board[5]}{board[6]}{board[7]}{board[8]}'] = [[], []]
for p in range(9):
    if board[p] == '_':
        O_Moves[f'{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}{board[5]}{board[6]}{board[7]}{board[8]}'][0].append(p)
        O_Moves[f'{board[0]}{board[1]}{board[2]}{board[3]}{board[4]}{board[5]}{board[6]}{board[7]}{board[8]}'][1].append(3)

# Turn 1 - X
for a in range(9):
    z = board[:]
    z[a] = 'X'
    #print(z)
    if check(z) == 'Stop':
        pass
    else:
        iters.append(z)
        iter1.append(z)
        X_Moves[f'{z[0]}{z[1]}{z[2]}{z[3]}{z[4]}{z[5]}{z[6]}{z[7]}{z[8]}'] = [[], []]
        indexz = []
        for p in range(9):
            if z[p] == '_':
                indexz.append(p)
                X_Moves[f'{z[0]}{z[1]}{z[2]}{z[3]}{z[4]}{z[5]}{z[6]}{z[7]}{z[8]}'][0].append(p)
                X_Moves[f'{z[0]}{z[1]}{z[2]}{z[3]}{z[4]}{z[5]}{z[6]}{z[7]}{z[8]}'][1].append(3)

# Turn 2 - O
        for b in range(8):
            y = z[:]
            y[indexz[b]] = 'O'
            #print(y)
            if check(y) == 'Stop':
                pass
            else:
                iters.append(y)
                iter2.append(y)
                O_Moves[f'{y[0]}{y[1]}{y[2]}{y[3]}{y[4]}{y[5]}{y[6]}{y[7]}{y[8]}'] = [[], []]
                indexy = []
                for p in range(9):
                    if y[p] == '_':
                        indexy.append(p)
                        O_Moves[f'{y[0]}{y[1]}{y[2]}{y[3]}{y[4]}{y[5]}{y[6]}{y[7]}{y[8]}'][0].append(p)
                        O_Moves[f'{y[0]}{y[1]}{y[2]}{y[3]}{y[4]}{y[5]}{y[6]}{y[7]}{y[8]}'][1].append(3)

# Turn 3 - X
                for c in range(7):
                    x = y[:]
                    x[indexy[c]] = 'X'
                    #print(x)
                    if check(x) == 'Stop':
                        pass
                    elif check(x) == 'Win':
                        iters.append(x)
                        iter3.append(x)
                        pass
                    else:
                        iters.append(x)
                        iter3.append(x)
                        X_Moves[f'{x[0]}{x[1]}{x[2]}{x[3]}{x[4]}{x[5]}{x[6]}{x[7]}{x[8]}'] = [[], []]
                        indexx = []
                        for p in range(9):
                            if x[p] == '_':
                                indexx.append(p)
                                X_Moves[f'{x[0]}{x[1]}{x[2]}{x[3]}{x[4]}{x[5]}{x[6]}{x[7]}{x[8]}'][0].append(p)
                                X_Moves[f'{x[0]}{x[1]}{x[2]}{x[3]}{x[4]}{x[5]}{x[6]}{x[7]}{x[8]}'][1].append(3)

# Turn 4 - O
                        for d in range(6):
                            w = x[:]
                            w[indexx[d]] = 'O'
                            #print(w)
                            if check(w) == 'Stop':
                                pass
                            elif check(w) == 'Win':
                                iters.append(w)
                                iter4.append(w)
                                pass
                            else:
                                iters.append(w)
                                iter4.append(w)
                                O_Moves[f'{w[0]}{w[1]}{w[2]}{w[3]}{w[4]}{w[5]}{w[6]}{w[7]}{w[8]}'] = [[], []]
                                indexw = []
                                for p in range(9):
                                    if w[p] == '_':
                                        indexw.append(p)
                                        O_Moves[f'{w[0]}{w[1]}{w[2]}{w[3]}{w[4]}{w[5]}{w[6]}{w[7]}{w[8]}'][0].append(p)
                                        O_Moves[f'{w[0]}{w[1]}{w[2]}{w[3]}{w[4]}{w[5]}{w[6]}{w[7]}{w[8]}'][1].append(3)

# Turn 5 - X
                                for e in range(5):
                                    v = w[:]
                                    v[indexw[e]] = 'X'
                                    #print(v)
                                    if check(v) == 'Stop':
                                        pass
                                    elif check(v) == 'Win':
                                        iters.append(v)
                                        iter5.append(v)
                                        pass
                                    else:
                                        iters.append(v)
                                        iter5.append(v)
                                        X_Moves[f'{v[0]}{v[1]}{v[2]}{v[3]}{v[4]}{v[5]}{v[6]}{v[7]}{v[8]}'] = [[], []]
                                        indexv = []
                                        for p in range(9):
                                            if v[p] == '_':
                                                indexv.append(p)
                                                X_Moves[f'{v[0]}{v[1]}{v[2]}{v[3]}{v[4]}{v[5]}{v[6]}{v[7]}{v[8]}'][
                                                    0].append(p)
                                                X_Moves[f'{v[0]}{v[1]}{v[2]}{v[3]}{v[4]}{v[5]}{v[6]}{v[7]}{v[8]}'][
                                                    1].append(3)

# Turn 6 - O
                                        for f in range(4):
                                            u = v[:]
                                            u[indexv[f]] = 'O'
                                            #print(u)
                                            if check(u) == 'Stop':
                                                pass
                                            elif check(u) == 'Win':
                                                iters.append(u)
                                                iter6.append(u)
                                                pass
                                            else:
                                                iters.append(u)
                                                iter6.append(u)
                                                O_Moves[f'{u[0]}{u[1]}{u[2]}{u[3]}{u[4]}{u[5]}{u[6]}{u[7]}{u[8]}'] = [[], []]
                                                indexu = []
                                                for p in range(9):
                                                    if u[p] == '_':
                                                        indexu.append(p)
                                                        O_Moves[f'{u[0]}{u[1]}{u[2]}{u[3]}{u[4]}{u[5]}{u[6]}{u[7]}{u[8]}'][0].append(p)
                                                        O_Moves[f'{u[0]}{u[1]}{u[2]}{u[3]}{u[4]}{u[5]}{u[6]}{u[7]}{u[8]}'][1].append(3)

# Turn 7 - X
                                                for g in range(3):
                                                    t = u[:]
                                                    t[indexu[g]] = 'X'
                                                    #print(t)
                                                    if check(t) == 'Stop':
                                                        pass
                                                    elif check(t) == 'Win':
                                                        iters.append(t)
                                                        iter7.append(t)
                                                        pass
                                                    else:
                                                        iters.append(t)
                                                        iter7.append(t)
                                                        X_Moves[
                                                            f'{t[0]}{t[1]}{t[2]}{t[3]}{t[4]}{t[5]}{t[6]}{t[7]}{t[8]}'] = [
                                                            [], []]
                                                        indext = []
                                                        for p in range(9):
                                                            if t[p] == '_':
                                                                indext.append(p)
                                                                X_Moves[
                                                                    f'{t[0]}{t[1]}{t[2]}{t[3]}{t[4]}{t[5]}{t[6]}{t[7]}{t[8]}'][
                                                                    0].append(p)
                                                                X_Moves[
                                                                    f'{t[0]}{t[1]}{t[2]}{t[3]}{t[4]}{t[5]}{t[6]}{t[7]}{t[8]}'][
                                                                    1].append(3)

# Turn 8 - O
                                                        for h in range(2):
                                                            s = t[:]
                                                            s[indext[h]] = 'O'
                                                            #print(s)
                                                            if check(s) == 'Stop':
                                                                pass
                                                            elif check(s) == 'Win':
                                                                iters.append(s)
                                                                iter8.append(s)
                                                                pass
                                                            else:
                                                                iters.append(s)
                                                                iter8.append(s)
                                                                O_Moves[f'{s[0]}{s[1]}{s[2]}{s[3]}{s[4]}{s[5]}{s[6]}{s[7]}{s[8]}'] = [[], []]
                                                                indexs = []
                                                                for p in range(9):
                                                                    if s[p] == '_':
                                                                        indexs.append(p)
                                                                        O_Moves[f'{s[0]}{s[1]}{s[2]}{s[3]}{s[4]}{s[5]}{s[6]}{s[7]}{s[8]}'][
                                                                            0].append(p)
                                                                        O_Moves[f'{s[0]}{s[1]}{s[2]}{s[3]}{s[4]}{s[5]}{s[6]}{s[7]}{s[8]}'][
                                                                            1].append(3)

# Turn 9 - X
                                                                for i in range(1):
                                                                    r = s[:]
                                                                    r[indexs[i]] = 'X'
                                                                    #print(r)
                                                                    if check(r) == 'Stop':
                                                                        pass
                                                                    elif check(r) == 'Win':
                                                                        iters.append(r)
                                                                        iter9.append(r)
                                                                        pass
                                                                    else:
                                                                        iters.append(r)
                                                                        iter9.append(r)

move_x = iter1 + iter3 + iter5 + iter7 + iter9
move_o = iter2 + iter4 + iter6 + iter8

#print(f'\nAll moves: {len(iters)}')
#print(f'X_Moves: {len(move_x)}')
#print(f'O_Moves: {len(move_o)}')

#print(O_Moves)
"""
with open("TrainingData/Adversary_DiMaggio_TTT_OMove.py", "w") as OMoveTable:
    OMoveTable.write('class Dictionary:\n')
    OMoveTable.write(f'\tstates = {O_Moves}')

with open("TrainingData/Adversary_DiMaggio_TTT_XMove.py", "w") as XMoveTable:
    XMoveTable.write('class Dictionary:\n')
    XMoveTable.write(f'\tstates = {X_Moves}')
"""
with open("TrainingData/RNG_DiMaggio_TTT_OMove.py", "w") as OMoveTable:
    OMoveTable.write('class Dictionary:\n')
    OMoveTable.write(f'\tstates = {O_Moves}')

with open("TrainingData/RNG_DiMaggio_TTT_XMove.py", "w") as XMoveTable:
    XMoveTable.write('class Dictionary:\n')
    XMoveTable.write(f'\tstates = {X_Moves}')
"""
with open("TrainingData/Human_DiMaggio_TTT_OMove.py", "w") as OMoveTable:
    OMoveTable.write('class Dictionary:\n')
    OMoveTable.write(f'\tstates = {O_Moves}')

with open("TrainingData/Human_DiMaggio_TTT_XMove.py", "w") as XMoveTable:
    XMoveTable.write('class Dictionary:\n')
    XMoveTable.write(f'\tstates = {X_Moves}')
"""
