class Dictionary:
	states = {'_________': [[0, 1, 2, 3, 4, 5, 6, 7, 8], [130277, 23922, 30088, 4002, 373406, 6456, 59710, 70150, 303334]], 'XO_______': [[2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 4, 5, 7, 5]], 'XOXO_____': [[4, 5, 6, 7, 8], [3, 3, 3, 3, 3]], 'XOXOXO___': [[6, 7, 8], [3, 7, 3]], 'XOXOXOOX_': [[8], [43]], 'XOXOXO_XO': [[6], [23]], 'XOXOX_O__': [[5, 7, 8], [6, 4, 13]], 'XOXOXXOO_': [[8], [23]], 'XOXOXXO_O': [[7], [1736]], 'XOXOX_OXO': [[5], [21309]], 'XOXOX__O_': [[5, 6, 8], [9, 5, 3]], 'XOXOXX_OO': [[6], [21]], 'XOXOX___O': [[5, 6, 7], [8, 11, 6]], 'XOXOOX___': [[6, 7, 8], [1, 4, 43]], 'XOXOOXX_O': [[7], [31763]], 'XOXOOXOX_': [[8], [45]], 'XOXOOX_XO': [[6], [125725]], 'XOXO_XO__': [[4, 7, 8], [4, 10, 11]], 'XOXO_XOXO': [[4], [329]], 'XOXO_X_O_': [[4, 6, 8], [3, 3, 3]], 'XOXO_XXOO': [[4], [39]], 'XOXO_X__O': [[4, 6, 7], [10, 28, 4]], 'XOXOO_X__': [[5, 7, 8], [1, 5, 0]], 'XOXOO_XXO': [[5], [23656]], 'XOXO_OX__': [[4, 7, 8], [3, 3, 3]], 'XOXO_OXXO': [[4], [39]], 'XOXO_OXOX': [[4], [3]], 'XOXO__XO_': [[4, 5, 8], [11, 3, 3]], 'XOXO__X_O': [[4, 5, 7], [493, 18, 33]], 'XOXOO__X_': [[5, 6, 8], [68124, 2, 0]], 'XOXOO_OXX': [[5], [39]], 'XOXO_O_X_': [[4, 6, 8], [3, 2, 3]], 'XOXO__OX_': [[4, 5, 8], [7, 3, 17]], 'XOXO___XO': [[4, 5, 6], [7, 4, 14]], 'XOXOO___X': [[5, 6, 7], [23, 1, 1]], 'XOXO__O_X': [[4, 5, 7], [11, 143, 31]], 'XOXO___OX': [[4, 5, 6], [3, 3, 3]], 'XOX_O____': [[3, 5, 6, 7, 8], [96, 0, 0, 212265, 0]], 'XOXXOO___': [[6, 7, 8], [29, 6, 5]], 'XOXXOOOX_': [[8], [200466]], 'XOXXOO_XO': [[6], [29]], 'XOXXO_O__': [[5, 7, 8], [0, 150658, 2]], 'XOXXOXO_O': [[7], [28]], 'XOXXO_OXO': [[5], [51557]], 'XOXXO___O': [[5, 6, 7], [3, 49, 14]], 'XOX_OXO__': [[3, 7, 8], [2, 13, 23]], 'XOX_OXOXO': [[3], [178371]], 'XOX_OX__O': [[3, 6, 7], [0, 0, 185916]], 'XOX_OOX__': [[3, 7, 8], [9, 1, 1]], 'XOX_OOXXO': [[3], [43]], 'XOX_O_X_O': [[3, 5, 7], [51, 2, 17]], 'XOX_OO_X_': [[3, 6, 8], [64981, 0, 0]], 'XOX_O_OX_': [[3, 5, 8], [16563, 2365, 26277]], 'XOX_O__XO': [[3, 5, 6], [11675, 10125, 23090]], 'XOX_O_O_X': [[3, 5, 7], [5, 91, 29]], 'XOX__O___': [[3, 4, 6, 7, 8], [5, 5, 3, 3, 3]], 'XOXX_OO__': [[4, 7, 8], [19, 18, 14]], 'XOXXXOOO_': [[8], [15]], 'XOXXXOO_O': [[7], [1022]], 'XOXX_OOXO': [[4], [367]], 'XOXX_O_O_': [[4, 6, 8], [5, 5, 5]], 'XOXXXO_OO': [[6], [19]], 'XOXX_O__O': [[4, 6, 7], [8, 49, 9]], 'XOX_XOO__': [[3, 7, 8], [11, 5, 27]], 'XOX_XOOXO': [[3], [17072]], 'XOX_XO_O_': [[3, 6, 8], [3, 3, 5]], 'XOX_XO__O': [[3, 6, 7], [40, 127, 17]], 'XOX__OXO_': [[3, 4, 8], [3, 9, 3]], 'XOX__OX_O': [[3, 4, 7], [15, 3, 19]], 'XOX__OOX_': [[3, 4, 8], [12, 65, 59]], 'XOX__O_XO': [[3, 4, 6], [3, 8, 27]], 'XOX___O__': [[3, 4, 5, 7, 8], [15, 72, 25, 11, 391]], 'XOXX__OO_': [[4, 5, 8], [3, 1, 2]], 'XOXX__O_O': [[4, 5, 7], [0, 0, 23]], 'XOX_X_OO_': [[3, 5, 8], [2, 4, 7]], 'XOX_X_O_O': [[3, 5, 7], [0, 0, 281]], 'XOX__XOO_': [[3, 4, 8], [1, 4, 7]], 'XOX__XO_O': [[3, 4, 7], [2, 0, 18]], 'XOX___OXO': [[3, 4, 5], [327, 102, 371]], 'XOX___OOX': [[3, 4, 5], [2, 31, 171]], 'XOX____O_': [[3, 4, 5, 6, 8], [2, 3, 5, 6, 3]], 'XOXX___OO': [[4, 5, 6], [4, 2, 5]], 'XOX_X__OO': [[3, 5, 6], [1, 3, 11]], 'XOX__X_OO': [[3, 4, 6], [1, 4, 1]], 'XOX___XOO': [[3, 4, 5], [217, 247, 0]], 'XOX_____O': [[3, 4, 5, 6, 7], [8, 130, 42, 990, 201]], 'XOOX_____': [[4, 5, 6, 7, 8], [163, 24, 225, 4, 38]], 'XOOXXO___': [[6, 7, 8], [25, 1, 85]], 'XOOXXOOX_': [[8], [35]], 'XOOXX_O__': [[5, 7, 8], [5, 9, 9]], 'XOOXX_OXO': [[5], [33]], 'XOOXX__O_': [[5, 6, 8], [5, 13, 3]], 'XOOXX___O': [[5, 6, 7], [25, 119, 2]], 'XOOXOX___': [[6, 7, 8], [13, 3, 2]], 'XOOXOX_XO': [[6], [73]], 'XOOX_XO__': [[4, 7, 8], [13, 0, 1]], 'XOOX_XOXO': [[4], [87]], 'XOOX_XOOX': [[4], [7]], 'XOOX_X_O_': [[4, 6, 8], [9, 9, 2]], 'XOOX_X__O': [[4, 6, 7], [3, 33, 11]], 'XOOXO__X_': [[5, 6, 8], [0, 13, 1]], 'XOOXOO_XX': [[6], [43]], 'XOOX_O_X_': [[4, 6, 8], [2, 3, 9]], 'XOOX_OOXX': [[4], [35]], 'XOOX__OX_': [[4, 5, 8], [17, 1, 1]], 'XOOX___XO': [[4, 5, 6], [5, 3, 5]], 'XOOXO___X': [[5, 6, 7], [1, 33, 1]], 'XOOX_O__X': [[4, 6, 7], [3, 9, 7]], 'XOOX__O_X': [[4, 5, 7], [47, 1, 0]], 'XOOX___OX': [[4, 5, 6], [13, 2, 11]], 'XO_XO____': [[2, 5, 6, 7, 8], [11, 1, 97, 16, 0]], 'XO_XOXO__': [[2, 7, 8], [3, 1, 1]], 'XO_XOXOXO': [[2], [350]], 'XO_XOX__O': [[2, 6, 7], [2, 17, 10]], 'XO_XOO_X_': [[2, 6, 8], [9, 19, 3]], 'XO_XOOOXX': [[2], [90]], 'XO_XO_OX_': [[2, 5, 8], [106, 0, 2]], 'XO_XO__XO': [[2, 5, 6], [4, 3, 17]], 'XO_XOO__X': [[2, 6, 7], [3, 15, 3]], 'XO_XO_O_X': [[2, 5, 7], [5, 0, 1]], 'XO_X_O___': [[2, 4, 6, 7, 8], [11, 5, 5, 3, 4]], 'XO_XXOO__': [[2, 7, 8], [11, 3, 5]], 'XO_XXOOXO': [[2], [60935]], 'XO_XXO_O_': [[2, 6, 8], [3, 3, 5]], 'XO_XXO__O': [[2, 6, 7], [3, 21, 3]], 'XO_X_OOX_': [[2, 4, 8], [12, 8, 6]], 'XO_X_O_XO': [[2, 4, 6], [5, 4, 5]], 'XO_X_OO_X': [[2, 4, 7], [6, 5, 5]], 'XO_X_O_OX': [[2, 4, 6], [3, 3, 3]], 'XO_X__O__': [[2, 4, 5, 7, 8], [9, 4, 3, 4, 2]], 'XO_XX_OO_': [[2, 5, 8], [4, 3, 5]], 'XO_XX_O_O': [[2, 5, 7], [1, 23, 3]], 'XO_X_XOO_': [[2, 4, 8], [2, 5, 3]], 'XO_X_XO_O': [[2, 4, 7], [3, 25, 16]], 'XO_X__OXO': [[2, 4, 5], [8, 64, 29]], 'XO_X__OOX': [[2, 4, 5], [2, 7, 1]], 'XO_X___O_': [[2, 4, 5, 6, 8], [3, 3, 3, 3, 3]], 'XO_XX__OO': [[2, 5, 6], [1, 7, 33]], 'XO_X_X_OO': [[2, 4, 6], [0, 7, 15]], 'XO_X____O': [[2, 4, 5, 6, 7], [3, 5, 5, 9, 3]], 'XOO_X____': [[3, 5, 6, 7, 8], [15, 14, 4, 7, 7]], 'XOOOXX___': [[6, 7, 8], [7, 4, 9]], 'XOOOXXOX_': [[8], [75]], 'XOOOXX_XO': [[6], [67036]], 'XOO_XXO__': [[3, 7, 8], [5, 11, 5]], 'XOO_XXOXO': [[3], [71]], 'XOO_XX_O_': [[3, 6, 8], [5, 3, 3]], 'XOO_XXXOO': [[3], [43]], 'XOO_XX__O': [[3, 6, 7], [295, 111, 77]], 'XOO_XOX__': [[3, 7, 8], [3, 4, 7]], 'XOO_X_XO_': [[3, 5, 8], [7, 11, 3]], 'XOO_X_X_O': [[3, 5, 7], [151, 20, 0]], 'XOOOX__X_': [[5, 6, 8], [159, 459, 833]], 'XOO_XO_X_': [[3, 6, 8], [1, 3, 29]], 'XOO_X_OX_': [[3, 5, 8], [13, 29, 3]], 'XOO_X__XO': [[3, 5, 6], [0, 21550, 0]], 'XO_OX____': [[2, 5, 6, 7, 8], [9, 3, 6, 3, 5]], 'XO_OXXO__': [[2, 7, 8], [7, 3, 9]], 'XO_OXXOXO': [[2], [139311]], 'XO_OXX_O_': [[2, 6, 8], [3, 3, 5]], 'XO_OXX__O': [[2, 6, 7], [1655, 1324, 756]], 'XO_OXO_X_': [[2, 6, 8], [3, 3, 7]], 'XO_OX_OX_': [[2, 5, 8], [41, 37, 129]], 'XO_OX__XO': [[2, 5, 6], [424, 395, 497]], 'XO__XO___': [[2, 3, 6, 7, 8], [5, 5, 3, 5, 3]], 'XO__XOXO_': [[2, 3, 8], [5, 5, 3]], 'XO__XOX_O': [[2, 3, 7], [7, 11, 2]], 'XO__XOOX_': [[2, 3, 8], [18, 4, 33]], 'XO__XO_XO': [[2, 3, 6], [2343, 0, 0]], 'XO__X_O__': [[2, 3, 5, 7, 8], [4, 8, 9, 9, 5]], 'XO__XXOO_': [[2, 3, 8], [3, 7, 3]], 'XO__XXO_O': [[2, 3, 7], [2, 17, 5]], 'XO__X_OXO': [[2, 3, 5], [4384, 41909, 81250]], 'XO__X__O_': [[2, 3, 5, 6, 8], [3, 5, 3, 7, 5]], 'XO__XX_OO': [[2, 3, 6], [3, 3, 17]], 'XO__X_XOO': [[2, 3, 5], [29, 35, 29]], 'XO__X___O': [[2, 3, 5, 6, 7], [98, 62, 46, 208, 15]], 'XOO__X___': [[3, 4, 6, 7, 8], [3, 3, 3, 3, 3]], 'XOO_OXX__': [[3, 7, 8], [17, 3, 3]], 'XOO_OXXXO': [[3], [41]], 'XOO__XXO_': [[3, 4, 8], [7, 7, 3]], 'XOO__XX_O': [[3, 4, 7], [37, 9, 7]], 'XOOO_X_X_': [[4, 6, 8], [3, 4, 11]], 'XOOOOX_XX': [[6], [43]], 'XOOO_XOXX': [[4], [39]], 'XOO_OX_X_': [[3, 6, 8], [3, 13, 3]], 'XOO__XOX_': [[3, 4, 8], [2, 41, 1]], 'XOO__X_XO': [[3, 4, 6], [111, 110, 7]], 'XOOO_X__X': [[4, 6, 7], [5, 11, 5]], 'XOO_OX__X': [[3, 6, 7], [0, 0, 0]], 'XOO__XO_X': [[3, 4, 7], [3, 17, 2]], 'XO_O_X___': [[2, 4, 6, 7, 8], [3, 3, 5, 16, 2]], 'XO_OOX_X_': [[2, 6, 8], [9, 5, 27]], 'XO_OOXOXX': [[2], [55]], 'XO_O_XOX_': [[2, 4, 8], [9, 7, 33]], 'XO_O_X_XO': [[2, 4, 6], [6, 6, 7]], 'XO_OOX__X': [[2, 6, 7], [5, 2, 9]], 'XO_O_XO_X': [[2, 4, 7], [5, 5, 3]], 'XO__OX___': [[2, 3, 6, 7, 8], [0, 0, 0, 7043, 0]], 'XO__OXX_O': [[2, 3, 7], [1, 29, 4]], 'XO__OXOX_': [[2, 3, 8], [6713, 0, 0]], 'XO__OX_XO': [[2, 3, 6], [1281, 129, 735]], 'XO__OXO_X': [[2, 3, 7], [11, 2, 3]], 'XO___XO__': [[2, 3, 4, 7, 8], [3, 3, 6, 3, 5]], 'XO___XOXO': [[2, 3, 4], [300, 99, 36]], 'XO___X_O_': [[2, 3, 4, 6, 8], [3, 5, 5, 3, 3]], 'XO___XXOO': [[2, 3, 4], [3, 5, 9]], 'XO___X__O': [[2, 3, 4, 6, 7], [13, 32, 17, 14, 5]], 'XOO___X__': [[3, 4, 5, 7, 8], [277, 44, 60, 51, 17]], 'XOO_O_XX_': [[3, 5, 8], [25, 11, 27]], 'XOO__OXX_': [[3, 4, 8], [5, 2, 7]], 'XOO___XXO': [[3, 4, 5], [57, 1, 11]], 'XOO_O_X_X': [[3, 5, 7], [23, 4, 9]], 'XOO__OX_X': [[3, 4, 7], [3, 11, 5]], 'XO__O_X__': [[2, 3, 5, 7, 8], [5, 13, 4, 3, 3]], 'XO__OOXX_': [[2, 3, 8], [1, 7, 17]], 'XO__O_XXO': [[2, 3, 5], [22, 79, 18]], 'XO__OOX_X': [[2, 3, 7], [3, 9, 5]], 'XO___OX__': [[2, 3, 4, 7, 8], [6, 7, 5, 3, 5]], 'XO___OXXO': [[2, 3, 4], [5, 9, 1]], 'XO____XO_': [[2, 3, 4, 5, 8], [2, 3, 5, 5, 3]], 'XO____X_O': [[2, 3, 4, 5, 7], [5, 9, 3, 5, 3]], 'XOO____X_': [[3, 4, 5, 6, 8], [4, 3, 9, 5, 7]], 'XOOO___XX': [[4, 5, 6], [11, 9, 7]], 'XOO_O__XX': [[3, 5, 6], [3, 3, 21]], 'XOO__O_XX': [[3, 4, 6], [35, 13, 13]], 'XOO___OXX': [[3, 4, 5], [0, 19, 0]], 'XO_O___X_': [[2, 4, 5, 6, 8], [4, 3, 6, 7, 9]], 'XO_OO__XX': [[2, 5, 6], [0, 9, 19]], 'XO_O_O_XX': [[2, 4, 6], [3, 3, 5]], 'XO_O__OXX': [[2, 4, 5], [9, 5, 5]], 'XO__O__X_': [[2, 3, 5, 6, 8], [52, 6, 80, 64, 175]], 'XO__OO_XX': [[2, 3, 6], [2, 23, 47]], 'XO__O_OXX': [[2, 3, 5], [5262, 0, 0]], 'XO___O_X_': [[2, 3, 4, 6, 8], [7, 3, 10, 4, 3]], 'XO___OOXX': [[2, 3, 4], [27, 25, 27]], 'XO____OX_': [[2, 3, 4, 5, 8], [330, 96, 218, 97, 145]], 'XO_____XO': [[2, 3, 4, 5, 6], [3, 3, 13, 18, 11]], 'XOO_____X': [[3, 4, 5, 6, 7], [30, 43, 10, 29, 1]], 'XO_O____X': [[2, 4, 5, 6, 7], [7, 3, 3, 3, 5]], 'XO__O___X': [[2, 3, 5, 6, 7], [0, 2, 0, 0, 5103]], 'XO___O__X': [[2, 3, 4, 6, 7], [5, 5, 5, 3, 5]], 'XO____O_X': [[2, 3, 4, 5, 7], [51, 4, 21, 10, 3]], 'XO_____OX': [[2, 3, 4, 5, 6], [3, 5, 3, 3, 3]], 'X_O______': [[1, 3, 4, 5, 6, 7, 8], [0, 72, 29, 2, 177, 117, 256]], 'XXOO_____': [[4, 5, 6, 7, 8], [3, 3, 3, 3, 2]], 'XXOOXO___': [[6, 7, 8], [3, 5, 5]], 'XXOOX_O__': [[5, 7, 8], [91, 219, 279]], 'XXOOXXOO_': [[8], [59]], 'XXOOXXO_O': [[7], [73]], 'XXOOX__O_': [[5, 6, 8], [33, 11, 29]], 'XXOOXX_OO': [[6], [66643]], 'XXOOX___O': [[5, 6, 7], [3, 3, 9]], 'XXOOOX___': [[6, 7, 8], [72, 0, 0]], 'XXOOOX_XO': [[6], [1067]], 'XXOO_XO__': [[4, 7, 8], [5, 1, 1]], 'XXOO_XOXO': [[4], [113]], 'XXOO_X_O_': [[4, 6, 8], [5, 7, 4]], 'XXOO_X__O': [[4, 6, 7], [42, 33, 37]], 'XXOOO__X_': [[5, 6, 8], [-6, 0, -6]], 'XXOO_O_X_': [[4, 6, 8], [5, 3, 3]], 'XXOO_OOXX': [[4], [13]], 'XXOO__OX_': [[4, 5, 8], [23, 0, 0]], 'XXOO___XO': [[4, 5, 6], [5, 6, 1]], 'XXOOO___X': [[5, 6, 7], [2, 1, 1]], 'XXOO_O__X': [[4, 6, 7], [5, 2, 3]], 'XXOO__O_X': [[4, 5, 7], [73, 1, 0]], 'XXO_O____': [[3, 5, 6, 7, 8], [0, 0, 185294, 0, 0]], 'XXOXOO___': [[6, 7, 8], [103, 1, 1]], 'XXOXO__O_': [[5, 6, 8], [0, 49, 1]], 'XXOXOX_OO': [[6], [19]], 'XXOXO___O': [[5, 6, 7], [0, 51, 1]], 'XXO_OX_O_': [[3, 6, 8], [0, 15690, 0]], 'XXO_OXXOO': [[3], [43]], 'XXO_OX__O': [[3, 6, 7], [0, 7202, 0]], 'XXO_OOX__': [[3, 7, 8], [31, 1, 0]], 'XXO_O_XO_': [[3, 5, 8], [633, 250, 90]], 'XXO_O_X_O': [[3, 5, 7], [61, 10, 2]], 'XXO_OO_X_': [[3, 6, 8], [1, 2, 1]], 'XXO_O__XO': [[3, 5, 6], [-4, 0, -2]], 'XXO_OO__X': [[3, 6, 7], [-2, 0, -1]], 'XXO__O___': [[3, 4, 6, 7, 8], [3, 3, 2, 3, 3]], 'XXOX_OO__': [[4, 7, 8], [-1, 0, -1]], 'XXOXXOOO_': [[8], [15]], 'XXOX_O_O_': [[4, 6, 8], [3, 7, 7]], 'XXO_XOO__': [[3, 7, 8], [3, 7, 5]], 'XXO_XO_O_': [[3, 6, 8], [0, 1, 31]], 'XXO__OXO_': [[3, 4, 8], [3, 2, 7]], 'XXO__OOX_': [[3, 4, 8], [1, 21, 0]], 'XXO__OO_X': [[3, 4, 7], [0, 23, 2]], 'XXO___O__': [[3, 4, 5, 7, 8], [0, 1232, 0, 7, 1]], 'XXOX__OO_': [[4, 5, 8], [2, 0, 0]], 'XXOX__O_O': [[4, 5, 7], [-22, 0, -21]], 'XXO_X_OO_': [[3, 5, 8], [2, 3, 21]], 'XXO_X_O_O': [[3, 5, 7], [0, 0, 661]], 'XXO__XOO_': [[3, 4, 8], [-1, 0, -2]], 'XXO__XO_O': [[3, 4, 7], [-36, 0, -36]], 'XXO___OXO': [[3, 4, 5], [0, 239, 0]], 'XXO____O_': [[3, 4, 5, 6, 8], [1, 2, 6, 15, 10]], 'XXOX___OO': [[4, 5, 6], [2, 1, 13]], 'XXO_X__OO': [[3, 5, 6], [-49, 0, -38]], 'XXO__X_OO': [[3, 4, 6], [0, 0, 62]], 'XXO___XOO': [[3, 4, 5], [5, 1, 21]], 'XXO_____O': [[3, 4, 5, 6, 7], [0, 0, 35, 0, 0]], 'X_OXO____': [[1, 5, 6, 7, 8], [4, 3, 17, 3, 3]], 'X_OXOX_O_': [[1, 6, 8], [2, 5, 3]], 'X_OXOX__O': [[1, 6, 7], [1, 25, 1]], 'X_OXOO_X_': [[1, 6, 8], [1, 23, 3]], 'X_OXO__XO': [[1, 5, 6], [2, 1, 15]], 'X_OXOO__X': [[1, 6, 7], [3, 31, 0]], 'X_OX_O___': [[1, 4, 6, 7, 8], [2, 0, 59, 0, 5]], 'X_OXXOO__': [[1, 7, 8], [3, 2, 13]], 'X_OXXO_O_': [[1, 6, 8], [3, 3, 9]], 'X_OX_OOX_': [[1, 4, 8], [0, 0, 0]], 'X_OX_OO_X': [[1, 4, 7], [1, 27, 1]], 'X_OX__O__': [[1, 4, 5, 7, 8], [0, 21, 3, 4, 5]], 'X_OXX_OO_': [[1, 5, 8], [3, 7, 9]], 'X_OXX_O_O': [[1, 5, 7], [1, 29, 0]], 'X_OX_XOO_': [[1, 4, 8], [2, 5, 2]], 'X_OX_XO_O': [[1, 4, 7], [0, 37, 2]], 'X_OX__OXO': [[1, 4, 5], [-99, 0, -103]], 'X_OX___O_': [[1, 4, 5, 6, 8], [5, 5, 8, 3, 3]], 'X_OXX__OO': [[1, 5, 6], [0, 3, 11]], 'X_OX_X_OO': [[1, 4, 6], [2, 15, 25]], 'X_OX____O': [[1, 4, 5, 6, 7], [4, 0, 75, 415, 0]], 'X_OOX____': [[1, 5, 6, 7, 8], [17, 4, 19, 32, 9]], 'X_OOXXO__': [[1, 7, 8], [5, 3, 15]], 'X_OOXXOXO': [[1], [63]], 'X_OOXX_O_': [[1, 6, 8], [33, 38, 123]], 'X_OOXX__O': [[1, 6, 7], [47352, 22851, 37826]], 'X_OOXO_X_': [[1, 6, 8], [7, 2, 11]], 'X_OOX_OX_': [[1, 5, 8], [5, 11, 7]], 'X_OOX__XO': [[1, 5, 6], [33, 8, 1]], 'X_O_XO___': [[1, 3, 6, 7, 8], [1, 6, 0, 1, 69]], 'X_O_XOXO_': [[1, 3, 8], [3, 7, 7]], 'X_O_XOOX_': [[1, 3, 8], [21, 1, 7]], 'X_O_X_O__': [[1, 3, 5, 7, 8], [9, 2, 11, 3, 5]], 'X_O_XXOO_': [[1, 3, 8], [5, 9, 3]], 'X_O_XXO_O': [[1, 3, 7], [4, 7, 11]], 'X_O_X_OXO': [[1, 3, 5], [27, 1, 21]], 'X_O_X__O_': [[1, 3, 5, 6, 8], [7, 16, 5, 8, 15]], 'X_O_XX_OO': [[1, 3, 6], [0, 207, 103]], 'X_O_X_XOO': [[1, 3, 5], [3, 7, 5]], 'X_O_X___O': [[1, 3, 5, 6, 7], [0, 0, 43231, 1, 8]], 'X_OO_X___': [[1, 4, 6, 7, 8], [5, 5, 10, 4, 5]], 'X_OOOX_X_': [[1, 6, 8], [0, 444, 0]], 'X_OO_XOX_': [[1, 4, 8], [2, 21, 1]], 'X_OO_X_XO': [[1, 4, 6], [530, 317, 243]], 'X_OOOX__X': [[1, 6, 7], [4, 364, 0]], 'X_O_OX___': [[1, 3, 6, 7, 8], [2, 0, 3795, 0, 2]], 'X_O_OXXO_': [[1, 3, 8], [56, 173, 15]], 'X_O_OXX_O': [[1, 3, 7], [6, 29, 7]], 'X_O_OX_XO': [[1, 3, 6], [0, 0, 5704]], 'X_O__XO__': [[1, 3, 4, 7, 8], [1, 1, 8, 3, 25]], 'X_O__XOXO': [[1, 3, 4], [4, 1, 25]], 'X_O__X_O_': [[1, 3, 4, 6, 8], [3, 3, 3, 4, 2]], 'X_O__XXOO': [[1, 3, 4], [3, 17, 4]], 'X_O__X__O': [[1, 3, 4, 6, 7], [7, 20, 184, 241, 214]], 'X_O_O_X__': [[1, 3, 5, 7, 8], [7, 17, 7, 13, 4]], 'X_O_OOXX_': [[1, 3, 8], [3, 7, 7]], 'X_O_O_XXO': [[1, 3, 5], [0, 85, 16]], 'X_O_OOX_X': [[1, 3, 7], [3, 11, 7]], 'X_O__OX__': [[1, 3, 4, 7, 8], [5, 13, 2, 4, 7]], 'X_O___XO_': [[1, 3, 4, 5, 8], [3, 7, 5, 3, 3]], 'X_O___X_O': [[1, 3, 4, 5, 7], [1, 987, 1, 305, 1]], 'X_OO___X_': [[1, 4, 5, 6, 8], [1, 9, 6, 5, 28]], 'X_OOO__XX': [[1, 5, 6], [1, 0, 31]], 'X_OO_O_XX': [[1, 4, 6], [5, 5, 13]], 'X_O_O__X_': [[1, 3, 5, 6, 8], [2, 0, 0, 124, 1]], 'X_O_OO_XX': [[1, 3, 6], [2, 1, 25]], 'X_O__O_X_': [[1, 3, 4, 6, 8], [0, 0, 0, 0, 121]], 'X_O___OX_': [[1, 3, 4, 5, 8], [7, 2, 63, 1, 2]], 'X_O____XO': [[1, 3, 4, 5, 6], [0, 0, 0, 1198, 0]], 'X_OO____X': [[1, 4, 5, 6, 7], [6, 5, 15, 37, 27]], 'X_O_O___X': [[1, 3, 5, 6, 7], [1, 1, 2, 77, 3]], 'X_O__O__X': [[1, 3, 4, 6, 7], [1, 7, 11, 5, 7]], 'X_O___O_X': [[1, 3, 4, 5, 7], [3, 3, 9, 3, 3]], 'X__O_____': [[1, 2, 4, 5, 6, 7, 8], [3, 3, 6, 6, 5, 5, 5]], 'XX_OO____': [[2, 5, 6, 7, 8], [27, 5, 2, 2, 6]], 'XX_OOXO__': [[2, 7, 8], [19, 0, 0]], 'XX_OOXOXO': [[2], [103]], 'XX_OOX_O_': [[2, 6, 8], [27, 10, 10]], 'XX_OOX__O': [[2, 6, 7], [73, 48, 10]], 'XX_OO_OX_': [[2, 5, 8], [35, 0, 0]], 'XX_OO__XO': [[2, 5, 6], [17, 5, 2]], 'XX_O_O___': [[2, 4, 6, 7, 8], [3, 3, 5, 3, 3]], 'XX_OXOO__': [[2, 7, 8], [7, 11, 3]], 'XX_OXO_O_': [[2, 6, 8], [3, 7, 5]], 'XX_OXO__O': [[2, 6, 7], [7, 3, 3]], 'XX_O_OOX_': [[2, 4, 8], [5, 3, 5]], 'XX_O_O_XO': [[2, 4, 6], [3, 3, 3]], 'XX_O__O__': [[2, 4, 5, 7, 8], [9, 10, 2, 10, 5]], 'XX_OX_OO_': [[2, 5, 8], [3, 2, 9]], 'XX_OX_O_O': [[2, 5, 7], [5, 2, 5]], 'XX_O_XOO_': [[2, 4, 8], [7, 2, 3]], 'XX_O_XO_O': [[2, 4, 7], [5, 3, 13]], 'XX_O__OXO': [[2, 4, 5], [9, 3, 7]], 'XX_O___O_': [[2, 4, 5, 6, 8], [3, 7, 5, 3, 3]], 'XX_OX__OO': [[2, 5, 6], [11, 2, 7]], 'XX_O_X_OO': [[2, 4, 6], [13, 3, 4]], 'XX_O____O': [[2, 4, 5, 6, 7], [7, 3, 3, 3, 8]], 'X_XOO____': [[1, 5, 6, 7, 8], [39, 42, 2, 2, 5]], 'X_XOOXO__': [[1, 7, 8], [19, 7, 19]], 'X_XOOX_O_': [[1, 6, 8], [3, 4, 15]], 'X_XOO_OX_': [[1, 5, 8], [15, 11, 2]], 'X_XO__O__': [[1, 4, 5, 7, 8], [5, 5, 5, 3, 3]], 'X_XOX_OO_': [[1, 5, 8], [13, 1, 5]], 'X_XO_XOO_': [[1, 4, 8], [5, 2, 7]], 'X_XO___O_': [[1, 4, 5, 6, 8], [3, 7, 3, 5, 3]], 'X__OXO___': [[1, 2, 6, 7, 8], [3, 3, 3, 2, 7]], 'X__OXOOX_': [[1, 2, 8], [13, 3, 5]], 'X__OXO_XO': [[1, 2, 6], [3, 5, 2]], 'X__OX_O__': [[1, 2, 5, 7, 8], [3, 6, 2, 7, 7]], 'X__OXXOO_': [[1, 2, 8], [1, 2, 31]], 'X__OXXO_O': [[1, 2, 7], [0, 0, 33084]], 'X__OX_OXO': [[1, 2, 5], [13, 3, 5]], 'X__OX__O_': [[1, 2, 5, 6, 8], [3, 7, 3, 3, 3]], 'X__OXX_OO': [[1, 2, 6], [0, 0, 6304]], 'X__OX___O': [[1, 2, 5, 6, 7], [4, 9, 3, 3, 7]], 'X__OOX___': [[1, 2, 6, 7, 8], [8, 62, 6, 1, 21]], 'X__OOXOX_': [[1, 2, 8], [0, 33, 0]], 'X__OOX_XO': [[1, 2, 6], [478, 151, 150]], 'X__O_XO__': [[1, 2, 4, 7, 8], [1, 26, 10, 13, 4]], 'X__O_XOXO': [[1, 2, 4], [165, 48, 47]], 'X__O_X_O_': [[1, 2, 4, 6, 8], [8, 2, 11, 8, 5]], 'X__O_X__O': [[1, 2, 4, 6, 7], [3, 9, 10, 11, 6]], 'X__OO__X_': [[1, 2, 5, 6, 8], [0, 0, 441, 1, 0]], 'X__O_O_X_': [[1, 2, 4, 6, 8], [2, 3, 7, 3, 3]], 'X__O__OX_': [[1, 2, 4, 5, 8], [5, 10, 5, 4, 3]], 'X__O___XO': [[1, 2, 4, 5, 6], [4, 3, 9, 7, 4]], 'X__OO___X': [[1, 2, 5, 6, 7], [0, 2, 325, 0, 0]], 'X__O_O__X': [[1, 2, 4, 6, 7], [3, 2, 7, 3, 7]], 'X___O____': [[1, 2, 3, 5, 6, 7, 8], [166583, 103645, 105610, 25415, 108839, 3062, 5429]], 'XX__OO___': [[2, 3, 6, 7, 8], [33, 1, 2, 0, 0]], 'XX_XOOO__': [[2, 7, 8], [31, 1, 0]], 'XX_XOOOXO': [[2], [25]], 'XX_XOO_O_': [[2, 6, 8], [5, 7, 11]], 'XX_XOO__O': [[2, 6, 7], [77, 15, 1]], 'XX__OOX_O': [[2, 3, 7], [13, 5, 2]], 'XX__OOOX_': [[2, 3, 8], [17, 3, 1]], 'XX__OO_XO': [[2, 3, 6], [17, 1, 1]], 'XX__O_O__': [[2, 3, 5, 7, 8], [43, 3, 8, 1, 2]], 'XX_XO_OO_': [[2, 5, 8], [11, 1, 2]], 'XX_XO_O_O': [[2, 5, 7], [27, 0, 4]], 'XX__OXOO_': [[2, 3, 8], [23, 2, 1]], 'XX__OXO_O': [[2, 3, 7], [43, 0, 0]], 'XX__O_OXO': [[2, 3, 5], [31, 1, 0]], 'XX__O__O_': [[2, 3, 5, 6, 8], [11, 13, 4, 4, 2]], 'XX_XO__OO': [[2, 5, 6], [35, 1, 15]], 'XX__OX_OO': [[2, 3, 6], [27, 0, 9]], 'XX__O___O': [[2, 3, 5, 6, 7], [15, 3, 3, 11, 1]], 'X_X_O_O__': [[1, 3, 5, 7, 8], [17, 13, 11, 8, 2]], 'X_XXO_OO_': [[1, 5, 8], [33, 0, 0]], 'X_X_O__O_': [[1, 3, 5, 6, 8], [3, 3, 3, 11, 5]], 'X__XOO___': [[1, 2, 6, 7, 8], [3, 4, 23, 3, 4]], 'X__XOOOX_': [[1, 2, 8], [0, 83, 0]], 'X__XOO_XO': [[1, 2, 6], [5, 17, 3]], 'X__XO_O__': [[1, 2, 5, 7, 8], [0, 150240, 0, 0, 13]], 'X__XOXOO_': [[1, 2, 8], [1, 0, 1]], 'X__XOXO_O': [[1, 2, 7], [-2, 0, -1]], 'X__XO_OXO': [[1, 2, 5], [0, 593, 0]], 'X__XO__O_': [[1, 2, 5, 6, 8], [5, 3, 3, 5, 5]], 'X__XOX_OO': [[1, 2, 6], [3, 0, 5]], 'X__XO___O': [[1, 2, 5, 6, 7], [7, 3, 6, 5, 9]], 'X___OXO__': [[1, 2, 3, 7, 8], [0, 71, 7, 0, 9]], 'X___OXOXO': [[1, 2, 3], [0, 5610, 1]], 'X___OX_O_': [[1, 2, 3, 6, 8], [15599, 0, 0, 0, 0]], 'X___OX__O': [[1, 2, 3, 6, 7], [2294, 1509, 1, 4091, 4576]], 'X___OO_X_': [[1, 2, 3, 6, 8], [0, 0, 37, 2, 1]], 'X___O_OX_': [[1, 2, 3, 5, 8], [0, 3039, 0, 0, 0]], 'X___O__XO': [[1, 2, 3, 5, 6], [2, 15, 4, 11, 8]], 'X____O___': [[1, 2, 3, 4, 6, 7, 8], [3, 24, 6, 5, 33, 1, 30]], 'XX___OO__': [[2, 3, 4, 7, 8], [3, 5, 5, 3, 7]], 'XX_X_OOO_': [[2, 4, 8], [5, 2, 11]], 'XX_X_OO_O': [[2, 4, 7], [13, 1, 2]], 'XX__XOOO_': [[2, 3, 8], [3, 2, 13]], 'XX__XOO_O': [[2, 3, 7], [19, 2, 5]], 'XX___OOXO': [[2, 3, 4], [107, 0, 113]], 'XX___O_O_': [[2, 3, 4, 6, 8], [3, 6, 3, 3, 7]], 'XX_X_O_OO': [[2, 4, 6], [5, 3, 5]], 'XX__XO_OO': [[2, 3, 6], [7, 1, 4]], 'XX___O__O': [[2, 3, 4, 6, 7], [15, 3, 2, 6, 5]], 'X__X_OO__': [[1, 2, 4, 7, 8], [10, 48, 0, 3, 23]], 'X__XXOOO_': [[1, 2, 8], [3, 3, 7]], 'X__XXOO_O': [[1, 2, 7], [-7, 0, -9]], 'X__X_OOXO': [[1, 2, 4], [3, 50, 1]], 'X__X_O_O_': [[1, 2, 4, 6, 8], [7, 3, 3, 3, 5]], 'X__XXO_OO': [[1, 2, 6], [1, 2, 3]], 'X__X_O__O': [[1, 2, 4, 6, 7], [0, 53, 0, 19, 7]], 'X___XOO__': [[1, 2, 3, 7, 8], [11, 7, 4, 3, 7]], 'X___XOOXO': [[1, 2, 3], [21, 4, 1]], 'X___XO_O_': [[1, 2, 3, 6, 8], [2, 3, 3, 9, 3]], 'X___XO__O': [[1, 2, 3, 6, 7], [0, 201, 1, 1, 2]], 'X____OX_O': [[1, 2, 3, 4, 7], [2, 13, 19, 3, 1]], 'X____OOX_': [[1, 2, 3, 4, 8], [7, 3, 1, 14, 6]], 'X____O_XO': [[1, 2, 3, 4, 6], [1, 3, 5, 1, 4]], 'X_____O__': [[1, 2, 3, 4, 5, 7, 8], [11, 21, 7, 16, 14, 3, 54]], 'XX____OO_': [[2, 3, 4, 5, 8], [47, 4, 1, 1, 5]], 'XX____O_O': [[2, 3, 4, 5, 7], [1017, 9, 0, 0, 224]], 'X__X__OO_': [[1, 2, 4, 5, 8], [2, 3, 3, 3, 3]], 'X__X__O_O': [[1, 2, 4, 5, 7], [0, 0, 0, 0, 72]], 'X___X_OO_': [[1, 2, 3, 5, 8], [2, 8, 5, 2, 31]], 'X___X_O_O': [[1, 2, 3, 5, 7], [1, 0, 1, 0, 92317]], 'X____XOO_': [[1, 2, 3, 4, 8], [1, 3, 3, 6, 12]], 'X____XO_O': [[1, 2, 3, 4, 7], [0, 1, 8, 0, 531]], 'X_____OXO': [[1, 2, 3, 4, 5], [229, 56, 8, 71, 79]], 'X______O_': [[1, 2, 3, 4, 5, 6, 8], [7, 3, 4, 3, 5, 3, 5]], 'XX_____OO': [[2, 3, 4, 5, 6], [33, 1, 2, 2, 4]], 'X__X___OO': [[1, 2, 4, 5, 6], [4, 3, 2, 4, 33]], 'X___X__OO': [[1, 2, 3, 5, 6], [3, 5, 7, 6, 3]], 'X____X_OO': [[1, 2, 3, 4, 6], [5, 6, 1, 8, 24]], 'X_______O': [[1, 2, 3, 4, 5, 6, 7], [0, 2183, 21, 15, 497, 1269, 20]], 'OX_______': [[2, 3, 4, 5, 6, 7, 8], [3, 3, 7, 3, 3, 3, 5]], 'OXOX_____': [[4, 5, 6, 7, 8], [127, 5, 5, 2, 23]], 'OXOXXO___': [[6, 7, 8], [3, 39, 12]], 'OXOXX_O__': [[5, 7, 8], [29, 17, 7]], 'OXOXX__O_': [[5, 6, 8], [477, 170, 89]], 'OXOXX___O': [[5, 6, 7], [17, 2, 11]], 'OXOXOX___': [[6, 7, 8], [-4, 0, -3]], 'OXOX_XO__': [[4, 7, 8], [9, 3, 2]], 'OXOX_XOXO': [[4], [9]], 'OXOX_X_O_': [[4, 6, 8], [11, 6, 4]], 'OXOX_X__O': [[4, 6, 7], [17, 3, 4]], 'OXOXO__X_': [[5, 6, 8], [-6, 0, -4]], 'OXOX_O_X_': [[4, 6, 8], [3, 5, 11]], 'OXOX___XO': [[4, 5, 6], [9, 6, 1]], 'OX_XO____': [[2, 5, 6, 7, 8], [0, 0, 0, 0, 8643]], 'OX_XOXO__': [[2, 7, 8], [1, 2, 3]], 'OX_XOX_O_': [[2, 6, 8], [0, 0, 54]], 'OX_XOO_X_': [[2, 6, 8], [1, 0, 15]], 'OX_X_O___': [[2, 4, 6, 7, 8], [16, 32, 12, 12, 34]], 'OX_XXOO__': [[2, 7, 8], [53, 255, 87]], 'OX_XXO_O_': [[2, 6, 8], [18913, 19028, 3905]], 'OX_XXO__O': [[2, 6, 7], [13, 1, 11]], 'OX_X_O_XO': [[2, 4, 6], [2, 13, 0]], 'OX_X__O__': [[2, 4, 5, 7, 8], [6, 61, 4, 6, 14]], 'OX_XX_OO_': [[2, 5, 8], [2, 61, 20]], 'OX_XX_O_O': [[2, 5, 7], [2, 41, 3]], 'OX_X_XOO_': [[2, 4, 8], [2, 3, 9]], 'OX_X_XO_O': [[2, 4, 7], [1, 17, 2]], 'OX_X___O_': [[2, 4, 5, 6, 8], [4, 18, 10, 3, 3]], 'OX_XX__OO': [[2, 5, 6], [5, 11, 9]], 'OX_X_X_OO': [[2, 4, 6], [3, 7, 4]], 'OX_X____O': [[2, 4, 5, 6, 7], [0, 16, 6, 0, 0]], 'OXO_X____': [[3, 5, 6, 7, 8], [98, 81, 41, 91, 109]], 'OX_OX____': [[2, 5, 6, 7, 8], [2, 5, 3, 7, 5]], 'OX_OXX_O_': [[2, 6, 8], [0, 4169, 0]], 'OX_OXX__O': [[2, 6, 7], [1, 11, 15]], 'OX__XO___': [[2, 3, 6, 7, 8], [7, 5, 3, 7, 3]], 'OX__X_O__': [[2, 3, 5, 7, 8], [1, 23, 6, 89, 13]], 'OX__XXOO_': [[2, 3, 8], [0, 27, 1]], 'OX__XXO_O': [[2, 3, 7], [1, 19, 3]], 'OX__X__O_': [[2, 3, 5, 6, 8], [0, 29309, 4200, 57535, 7193]], 'OX__XX_OO': [[2, 3, 6], [2, 13, 9]], 'OX__X___O': [[2, 3, 5, 6, 7], [3, 5, 9, 3, 7]], 'OX_O_X___': [[2, 4, 6, 7, 8], [3, 5, 3, 3, 3]], 'OX_OOX_X_': [[2, 6, 8], [0, 6, 2]], 'OX__OX___': [[2, 3, 6, 7, 8], [0, 1, 1, 1, 431]], 'OX__OXOX_': [[2, 3, 8], [-17, 0, -19]], 'OX___XO__': [[2, 3, 4, 7, 8], [3, 3, 3, 2, 2]], 'OX___X_O_': [[2, 3, 4, 6, 8], [5, 3, 3, 3, 3]], 'OX___X__O': [[2, 3, 4, 6, 7], [1, 8, 26, 5, 2]], 'OXO____X_': [[3, 4, 5, 6, 8], [5, 5, 4, 7, 3]], 'OX_O___X_': [[2, 4, 5, 6, 8], [3, 9, 2, 5, 4]], 'OX__O__X_': [[2, 3, 5, 6, 8], [0, 0, 1, 1, 29]], 'OX___O_X_': [[2, 3, 4, 6, 8], [5, 4, 5, 3, 5]], 'OX____OX_': [[2, 3, 4, 5, 8], [2, 3, 19, 1, 1]], 'OX_____XO': [[2, 3, 4, 5, 6], [2, 1, 3, 3, 6]], '_XO______': [[0, 3, 4, 5, 6, 7, 8], [0, 1810, 1557, 229, 1480, 0, 1794]], '_XOXO____': [[0, 5, 6, 7, 8], [0, 0, 4996, 0, 0]], '_XOXOO_X_': [[0, 6, 8], [1, 4, 2]], '_XOX_O___': [[0, 4, 6, 7, 8], [4, 1, 7, 2, 280]], '_XOXXO_O_': [[0, 6, 8], [0, 0, 22494]], '_XOX___O_': [[0, 4, 5, 6, 8], [5, 61, 7, 115, 84]], '_XOXX__OO': [[0, 5, 6], [1, 23, 1]], '_XOX____O': [[0, 4, 5, 6, 7], [-78, 0, 0, 0, -83]], '_XOOX____': [[0, 5, 6, 7, 8], [5, 6, 4, 11, 5]], '_XO_XO___': [[0, 3, 6, 7, 8], [3, 5, 5, 3, 14]], '_XO_X_O__': [[0, 3, 5, 7, 8], [3, 8, 7, 5, 7]], '_XO_X__O_': [[0, 3, 5, 6, 8], [4, 22581, 13057, 20586, 34434]], '_XO_X___O': [[0, 3, 5, 6, 7], [1, 2, 211, 5, 143]], '_XOO___X_': [[0, 4, 5, 6, 8], [4, 9, 3, 6, 5]], '_XO_O__X_': [[0, 3, 5, 6, 8], [-15, 0, 0, 0, -16]], '_XO__O_X_': [[0, 3, 4, 6, 8], [3, 5, 3, 3, 2]], '_XO___OX_': [[0, 3, 4, 5, 8], [3, 3, 5, 3, 5]], '_X_O_____': [[0, 2, 4, 5, 6, 7, 8], [3, 3, 3, 5, 3, 7, 3]], '_X_OXO___': [[0, 2, 6, 7, 8], [11, 2, 5, 5, 3]], '_X_OX_O__': [[0, 2, 5, 7, 8], [5, 3, 11, 3, 3]], '_X_OXXOO_': [[0, 2, 8], [2, 2, 0]], '_X_OX__O_': [[0, 2, 5, 6, 8], [6, 4, 9, 6, 7]], '_X_OX___O': [[0, 2, 5, 6, 7], [3, 5, 3, 9, 7]], '_X_OOX___': [[0, 2, 6, 7, 8], [82, 49, 83, 37, 73]], '_X_O_XO__': [[0, 2, 4, 7, 8], [4, 2, 1, 1, 3]], '_X_O_X_O_': [[0, 2, 4, 6, 8], [4, 3, 7, 3, 3]], '_X_OO__X_': [[0, 2, 5, 6, 8], [3, 0, 14, 2, 0]], '_X_O_O_X_': [[0, 2, 4, 6, 8], [3, 2, 3, 3, 3]], '_X__O____': [[0, 2, 3, 5, 6, 7, 8], [18783, 44771, 13398, 0, 12710, 6, 354]], '_X_XOO___': [[0, 2, 6, 7, 8], [188, 42, 117, 6, 62]], '_X_XO___O': [[0, 2, 5, 6, 7], [63, 0, 1, 1, 0]], '_X___O___': [[0, 2, 3, 4, 6, 7, 8], [9, 21, 10, 21, 6, 13, 18]], '_X_X_O__O': [[0, 2, 4, 6, 7], [5, 2, 1, 1, 3]], '_X__XOO__': [[0, 2, 3, 7, 8], [5, 2, 3, 13, 3]], '_X__XO_O_': [[0, 2, 3, 6, 8], [8, 14, 2, 5, 12]], '_X__XO__O': [[0, 2, 3, 6, 7], [3, 50, 1, 0, 21]], '_X____O__': [[0, 2, 3, 4, 5, 7, 8], [2493, 171, 0, 1552, 0, 3, 1319]], '_X__X_OO_': [[0, 2, 3, 5, 8], [0, 0, 0, 0, 20021]], '_X__X_O_O': [[0, 2, 3, 5, 7], [3, 3, 1, 10, 31]], '_X_____O_': [[0, 2, 3, 4, 5, 6, 8], [50, 107, 6, 127, 6, 84, 105]], '_X__X__OO': [[0, 2, 3, 5, 6], [0, 0, 0, 0, 30475]], '_X______O': [[0, 2, 3, 4, 5, 6, 7], [139, 900, 0, 233, 90, 243, 14]], 'O___X____': [[1, 2, 3, 5, 6, 7, 8], [98315, 57043, 89669, 18504, 34072, 30460, 45238]], '_O__X____': [[0, 2, 3, 5, 6, 7, 8], [58, 21, 15, 31, 7, 7, 5]]}
