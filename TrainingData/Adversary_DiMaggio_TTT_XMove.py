class Dictionary:
	states = {'X________': [[1, 2, 3, 4, 5, 6, 7, 8], [0, 14, 0, 519087, 0, 0, 0, 54]], 'XOX______': [[3, 4, 5, 6, 7, 8], [3, 3, 3, 2, 3, 3]], 'XOXOX____': [[5, 6, 7, 8], [2, 2, 2, 3]], 'XOXOXO_X_': [[6, 8], [2, 2]], 'XOXOXXO__': [[7, 8], [1, 11]], 'XOXOX_OX_': [[5, 8], [0, 6341]], 'XOXOXX_O_': [[6, 8], [0, 1]], 'XOXOXX__O': [[6, 7], [1669, 0]], 'XOXOX__XO': [[5, 6], [0, 460]], 'XOXO_X___': [[4, 6, 7, 8], [3, 3, 3, 3]], 'XOXOOXX__': [[7, 8], [23, 5]], 'XOXOOX_X_': [[6, 8], [0, 68132]], 'XOXO_XOX_': [[4, 8], [1, 13]], 'XOXO_XXO_': [[4, 8], [3, 3]], 'XOXO_XX_O': [[4, 7], [117, 0]], 'XOXO_X_XO': [[4, 6], [5, 10]], 'XOXO__X__': [[4, 5, 7, 8], [3, 3, 2, 3]], 'XOXOO_XX_': [[5, 8], [39, 24]], 'XOXOO_X_X': [[5, 7], [11, 9]], 'XOXO_OXX_': [[4, 8], [5, 2]], 'XOXO_OX_X': [[4, 7], [3, 3]], 'XOXO__XXO': [[4, 5], [52, 0]], 'XOXO___X_': [[4, 5, 6, 8], [4, 3, 2, 6]], 'XOXOO__XX': [[5, 6], [21, 2]], 'XOXO__OXX': [[4, 5], [-11, -9]], 'XOXO____X': [[4, 5, 6, 7], [3, 1, 2, 3]], 'XOXXO____': [[5, 6, 7, 8], [0, 530, 913, 3]], 'XOXXOO_X_': [[6, 8], [64986, 0]], 'XOXXOXO__': [[7, 8], [17, 5]], 'XOXXO_OX_': [[5, 8], [134642, 32829]], 'XOXXO_O_X': [[5, 7], [111, 189]], 'XOXXOX__O': [[6, 7], [10, 31]], 'XOXXO__XO': [[5, 6], [0, 12122]], 'XOX_OX___': [[3, 6, 7, 8], [0, 6, 91, 19]], 'XOX_OXOX_': [[3, 8], [0, 9124]], 'XOX_OXX_O': [[3, 7], [7, 27]], 'XOX_OX_XO': [[3, 6], [41465, 155923]], 'XOX_O_X__': [[3, 5, 7, 8], [5, 7, 19, 1]], 'XOX_OOXX_': [[3, 8], [31, 0]], 'XOX_O_XXO': [[3, 5], [23478, 0]], 'XOX_O__X_': [[3, 5, 6, 8], [68152, 64994, 38039, 41192]], 'XOX_O_OXX': [[3, 5], [0, 31643]], 'XOX_O___X': [[3, 5, 6, 7], [0, 28, 0, 37]], 'XOXX_O___': [[4, 6, 7, 8], [1, 4, 1, 2]], 'XOXXXOO__': [[7, 8], [0, 523]], 'XOXX_OOX_': [[4, 8], [22, 21]], 'XOXXXO_O_': [[6, 8], [3, 2]], 'XOXXXO__O': [[6, 7], [495, 0]], 'XOXX_O_XO': [[4, 6], [2, 10]], 'XOX_XO___': [[3, 6, 7, 8], [3, 3, 2, 2]], 'XOX_XOOX_': [[3, 8], [0, 1397]], 'XOX_XO_XO': [[3, 6], [0, 2360]], 'XOX__OX__': [[3, 4, 7, 8], [3, 5, 2, 2]], 'XOX__OXXO': [[3, 4], [-10, -9]], 'XOX__O_X_': [[3, 4, 6, 8], [5, 5, 6, 2]], 'XOXX__O__': [[4, 5, 7, 8], [6, 13, 10, 23]], 'XOXXX_OO_': [[5, 8], [2, 9]], 'XOXX_XOO_': [[4, 8], [7, 9]], 'XOXX__OOX': [[4, 5], [13, 2]], 'XOXXX_O_O': [[5, 7], [4, 25]], 'XOXX_XO_O': [[4, 7], [9, 27]], 'XOXX__OXO': [[4, 5], [310, 285]], 'XOX_X_O__': [[3, 5, 7, 8], [4, 1, 3, 59]], 'XOX_XXOO_': [[3, 8], [1, 7]], 'XOX_XXO_O': [[3, 7], [4, 19]], 'XOX_X_OXO': [[3, 5], [14417, 13195]], 'XOX__XO__': [[3, 4, 7, 8], [1, 2, 5, 5]], 'XOX__XOXO': [[3, 4], [196, 520]], 'XOX___OX_': [[3, 4, 5, 8], [1, 64, 125, 153]], 'XOX___O_X': [[3, 4, 5, 7], [-83, 0, 0, -84]], 'XOXX___O_': [[4, 5, 6, 8], [5, 3, 3, 3]], 'XOXXX__OO': [[5, 6], [0, 23]], 'XOXX_X_OO': [[4, 6], [15, 3]], 'XOX_X__O_': [[3, 5, 6, 8], [3, 3, 3, 3]], 'XOX_XX_OO': [[3, 6], [1, 9]], 'XOX__X_O_': [[3, 4, 6, 8], [3, 3, 2, 2]], 'XOX__XXOO': [[3, 4], [0, 27]], 'XOX___XO_': [[3, 4, 5, 8], [2, 13, 1, 3]], 'XOX____OX': [[3, 4, 5, 6], [3, 3, 3, 3]], 'XOXX____O': [[4, 5, 6, 7], [3, 2, 10, 10]], 'XOX_X___O': [[3, 5, 6, 7], [4, 0, 233, 1]], 'XOX__X__O': [[3, 4, 6, 7], [16, 47, 32, 23]], 'XOX___X_O': [[3, 4, 5, 7], [-197, 0, 0, -217]], 'XOX____XO': [[3, 4, 5, 6], [12, 99, 0, 85]], 'XO_X_____': [[2, 4, 5, 6, 7, 8], [3, 4, 4, 10, 3, 1]], 'XOOXX____': [[5, 6, 7, 8], [-39, 0, 0, -54]], 'XOOXXO_X_': [[6, 8], [3, 19]], 'XOOXX_OX_': [[5, 8], [-7, -7]], 'XOOXX__XO': [[5, 6], [19, 1]], 'XOOX_X___': [[4, 6, 7, 8], [0, 8, 0, 0]], 'XOOXOX_X_': [[6, 8], [11, 1]], 'XOOXOX__X': [[6, 7], [5, 17]], 'XOOX_XOX_': [[4, 8], [29, 0]], 'XOOX_XO_X': [[4, 7], [21, 1]], 'XOOX_X_OX': [[4, 6], [11, 3]], 'XOOX_X_XO': [[4, 6], [-25, -30]], 'XOOX___X_': [[4, 5, 6, 8], [6, 4, 6, 3]], 'XOOXO__XX': [[5, 6], [1, 23]], 'XOOX_O_XX': [[4, 6], [-9, -6]], 'XOOX__OXX': [[4, 5], [33, 2]], 'XOOX____X': [[4, 5, 6, 7], [-5, 0, 0, -2]], 'XO_XOX___': [[2, 6, 7, 8], [1, 14, 31, 2]], 'XO_XOXOX_': [[2, 8], [29, 6]], 'XO_XOXO_X': [[2, 7], [7, 11]], 'XO_XOX_XO': [[2, 6], [0, 181]], 'XO_XO__X_': [[2, 5, 6, 8], [8, 3, 53, 0]], 'XO_XOO_XX': [[2, 6], [0, 24]], 'XO_XO_OXX': [[2, 5], [57, 21]], 'XO_XO___X': [[2, 5, 6, 7], [4, 1, 15, 27]], 'XO_XXO___': [[2, 6, 7, 8], [0, 3, 2, 1]], 'XO_XXOOX_': [[2, 8], [0, 18913]], 'XO_XXO_XO': [[2, 6], [25, 9]], 'XO_X_O_X_': [[2, 4, 6, 8], [3, 3, 3, 3]], 'XO_X_OOXX': [[2, 4], [0, 25]], 'XO_X_O__X': [[2, 4, 6, 7], [2, 2, 4, 3]], 'XO_XX_O__': [[2, 5, 7, 8], [2, 2, 2, 4]], 'XO_XX_OXO': [[2, 5], [0, 42014]], 'XO_X_XO__': [[2, 4, 7, 8], [3, 3, 3, 2]], 'XO_X_XOXO': [[2, 4], [0, 133]], 'XO_X__OX_': [[2, 4, 5, 8], [5, 79, 19, 22]], 'XO_X__O_X': [[2, 4, 5, 7], [3, 10, 3, 7]], 'XO_XX__O_': [[2, 5, 6, 8], [3, 3, 4, 3]], 'XO_X_X_O_': [[2, 4, 6, 8], [2, 3, 3, 5]], 'XO_X___OX': [[2, 4, 5, 6], [2, 3, 3, 3]], 'XO_XX___O': [[2, 5, 6, 7], [-5, 0, 0, -4]], 'XO_X_X__O': [[2, 4, 6, 7], [1, 0, 6, 0]], 'XO_X___XO': [[2, 4, 5, 6], [3, 3, 3, 3]], 'XO__X____': [[2, 3, 5, 6, 7, 8], [2, 0, 0, 5, 0, 5]], 'XOO_XX___': [[3, 6, 7, 8], [4, 2, 2, 6]], 'XOOOXX_X_': [[6, 8], [0, 4320]], 'XOO_XXOX_': [[3, 8], [-19, -15]], 'XOO_XXXO_': [[3, 8], [0, -1]], 'XOO_XXX_O': [[3, 7], [129, 0]], 'XOO_XX_XO': [[3, 6], [21742, 0]], 'XOO_X_X__': [[3, 5, 7, 8], [-10, 0, 0, -11]], 'XOO_XOXX_': [[3, 8], [2, 9]], 'XOO_X_XXO': [[3, 5], [9, 37]], 'XOO_X__X_': [[3, 5, 6, 8], [186, 0, 0, 18588]], 'XO_OXX___': [[2, 6, 7, 8], [4, 3, 3, 5]], 'XO_OXXOX_': [[2, 8], [0, 22526]], 'XO_OXX_XO': [[2, 6], [2760, 2296]], 'XO_OX__X_': [[2, 5, 6, 8], [1, 2, 3, 6]], 'XO__XOX__': [[2, 3, 7, 8], [3, 3, 3, 2]], 'XO__XOXXO': [[2, 3], [23, 1]], 'XO__XO_X_': [[2, 3, 6, 8], [0, 2, 4, 4]], 'XO__XXO__': [[2, 3, 7, 8], [1, 1, 2, 2]], 'XO__XXOXO': [[2, 3], [0, 81365]], 'XO__X_OX_': [[2, 3, 5, 8], [0, 7, 1, 34416]], 'XO__XX_O_': [[2, 3, 6, 8], [3, 3, 3, 1]], 'XO__XXXOO': [[2, 3], [-7, -10]], 'XO__X_XO_': [[2, 3, 5, 8], [2, 2, 2, 3]], 'XO__XX__O': [[2, 3, 6, 7], [5, 42, 2, 0]], 'XO__X_X_O': [[2, 3, 5, 7], [-32, 0, 0, -38]], 'XO__X__XO': [[2, 3, 5, 6], [2932, 1299, 2354, 657]], 'XO___X___': [[2, 3, 4, 6, 7, 8], [3, 3, 3, 5, 2, 3]], 'XOO__XX__': [[3, 4, 7, 8], [0, 0, 0, 0]], 'XOO_OXXX_': [[3, 8], [-3, -7]], 'XOO_OXX_X': [[3, 7], [1, 21]], 'XOO__XXXO': [[3, 4], [60, 0]], 'XOO__X_X_': [[3, 4, 6, 8], [2, 2, 2, 3]], 'XOOO_X_XX': [[4, 6], [-3, -3]], 'XOO_OX_XX': [[3, 6], [0, 23]], 'XOO__XOXX': [[3, 4], [2, 25]], 'XOO__X__X': [[3, 4, 6, 7], [1, 8, 1, 3]], 'XO_O_X_X_': [[2, 4, 6, 8], [2, 3, 3, 8]], 'XO_OOX_XX': [[2, 6], [-7, -9]], 'XO_O_XOXX': [[2, 4], [-6, -6]], 'XO_O_X__X': [[2, 4, 6, 7], [2, 5, 3, 3]], 'XO__OXX__': [[2, 3, 7, 8], [2, 3, 25, 1]], 'XO__OXXXO': [[2, 3], [0, 825]], 'XO__OX_X_': [[2, 3, 6, 8], [0, 0, 6671, 532]], 'XO__OXOXX': [[2, 3], [31, 0]], 'XO__OX__X': [[2, 3, 6, 7], [10, 2, 2, 15]], 'XO___XOX_': [[2, 3, 4, 8], [1, 1, 59, 81]], 'XO___XO_X': [[2, 3, 4, 7], [3, 2, 2, 2]], 'XO___XXO_': [[2, 3, 4, 8], [2, 3, 3, 3]], 'XO___XX_O': [[2, 3, 4, 7], [1, 5, 6, 1]], 'XO___X_XO': [[2, 3, 4, 6], [0, 7, 7, 6]], 'XO____X__': [[2, 3, 4, 5, 7, 8], [1, 1, 1, 1, 3, 1]], 'XOO___XX_': [[3, 4, 5, 8], [-7, 0, 0, -10]], 'XOO___X_X': [[3, 4, 5, 7], [-7, 0, 0, -6]], 'XO__O_XX_': [[2, 3, 5, 8], [-5, 0, 0, -2]], 'XO__O_X_X': [[2, 3, 5, 7], [0, 2, 2, 25]], 'XO___OXX_': [[2, 3, 4, 8], [5, 2, 3, 3]], 'XO___OX_X': [[2, 3, 4, 7], [2, 3, 3, 3]], 'XO____XXO': [[2, 3, 4, 5], [1, 34, 2, 1]], 'XO_____X_': [[2, 3, 4, 5, 6, 8], [1, 0, 34, 6, 16, 19]], 'XOO____XX': [[3, 4, 5, 6], [1, 5, 2, 8]], 'XO_O___XX': [[2, 4, 5, 6], [2, 1, 2, 1]], 'XO__O__XX': [[2, 3, 5, 6], [0, 0, 2, 5206]], 'XO___O_XX': [[2, 3, 4, 6], [2, 3, 3, 3]], 'XO____OXX': [[2, 3, 4, 5], [1, 0, 71, 29]], 'XO______X': [[2, 3, 4, 5, 6, 7], [3, 3, 3, 2, 3, 2]], 'XXO______': [[3, 4, 5, 6, 7, 8], [5, 6, 5, 5, 5, 7]], 'XXOOX____': [[5, 6, 7, 8], [2, 1, 6, 1]], 'XXOOXXO__': [[7, 8], [-19, -24]], 'XXOOXX_O_': [[6, 8], [0, 19084]], 'XXOOXX__O': [[6, 7], [0, 47552]], 'XXOO_X___': [[4, 6, 7, 8], [3, 4, 3, 4]], 'XXOOOX_X_': [[6, 8], [51, 9]], 'XXOOOX__X': [[6, 7], [67, 29]], 'XXOO_XOX_': [[4, 8], [17, 2]], 'XXOO_XO_X': [[4, 7], [33, 0]], 'XXOO_X_XO': [[4, 6], [564, 0]], 'XXOO___X_': [[4, 5, 6, 8], [12, 2, 3, 3]], 'XXOOO__XX': [[5, 6], [19, 17]], 'XXOO_O_XX': [[4, 6], [7, 0]], 'XXOO__OXX': [[4, 5], [31, 1]], 'XXOO____X': [[4, 5, 6, 7], [10, 5, 6, 2]], 'XXOXO____': [[5, 6, 7, 8], [1, 59, 0, 1]], 'XXOXOO_X_': [[6, 8], [19, 3]], 'XXOXOO__X': [[6, 7], [31, 1]], 'XXOXOX_O_': [[6, 8], [31, 1]], 'XXOXOX__O': [[6, 7], [33, 1]], 'XXOXO__XO': [[5, 6], [29, 41]], 'XXO_OX___': [[3, 6, 7, 8], [13, 37, 9, 6]], 'XXO_OXXO_': [[3, 8], [16132, 0]], 'XXO_OXX_O': [[3, 7], [12813, 0]], 'XXO_OX_XO': [[3, 6], [10, 49]], 'XXO_O_X__': [[3, 5, 7, 8], [185874, 0, 30, 0]], 'XXO_OOXX_': [[3, 8], [11, 7]], 'XXO_OOX_X': [[3, 7], [17, 3]], 'XXO_O_XXO': [[3, 5], [13, 47]], 'XXO_O__X_': [[3, 5, 6, 8], [41, 9, 11, 16]], 'XXO_OO_XX': [[3, 6], [13, 13]], 'XXO_O___X': [[3, 5, 6, 7], [7, 18, 3, 6]], 'XXOX_O___': [[4, 6, 7, 8], [1, 18, 4, 7]], 'XXOXXOO__': [[7, 8], [3, 13]], 'XXOX_OOX_': [[4, 8], [3, 19]], 'XXOX_OO_X': [[4, 7], [33, 1]], 'XXOXXO_O_': [[6, 8], [2, 19]], 'XXO_XO___': [[3, 6, 7, 8], [3, 3, 3, 7]], 'XXO_XOXO_': [[3, 8], [1, 23]], 'XXO__OX__': [[3, 4, 7, 8], [2, 2, 2, 7]], 'XXO__O_X_': [[3, 4, 6, 8], [3, 5, 5, 5]], 'XXO__O__X': [[3, 4, 6, 7], [3, 5, 5, 3]], 'XXOX__O__': [[4, 5, 7, 8], [9, 9, 7, 3]], 'XXOXX_OO_': [[5, 8], [1, 19]], 'XXOX_XOO_': [[4, 8], [9, 19]], 'XXOXX_O_O': [[5, 7], [55, 15]], 'XXOX_XO_O': [[4, 7], [13, 87]], 'XXOX__OXO': [[4, 5], [221, 47]], 'XXO_X_O__': [[3, 5, 7, 8], [-284, 0, 0, -314]], 'XXO_XXOO_': [[3, 8], [2, 13]], 'XXO_XXO_O': [[3, 7], [1, 23]], 'XXO__XO__': [[3, 4, 7, 8], [3, 11, 7, 7]], 'XXO__XOXO': [[3, 4], [0, 97]], 'XXO___OX_': [[3, 4, 5, 8], [4, 35, 3, 1]], 'XXO___O_X': [[3, 4, 5, 7], [1, 19, 9, 7]], 'XXOX___O_': [[4, 5, 6, 8], [7, 2, 15, 2]], 'XXOXX__OO': [[5, 6], [111, 11]], 'XXOX_X_OO': [[4, 6], [1, 19]], 'XXO_X__O_': [[3, 5, 6, 8], [16, 0, 0, 300]], 'XXO_XX_OO': [[3, 6], [9, 33]], 'XXO_X_XOO': [[3, 5], [61, 211]], 'XXO__X_O_': [[3, 4, 6, 8], [9, 13, 13, 4]], 'XXO__XXOO': [[3, 4], [119, 0]], 'XXO___XO_': [[3, 4, 5, 8], [14, 1, 4, 5]], 'XXOX____O': [[4, 5, 6, 7], [0, 121, 91, 5]], 'XXO_X___O': [[3, 5, 6, 7], [2, 23, 2, 7]], 'XXO__X__O': [[3, 4, 6, 7], [42, 33, 156, 62]], 'XXO___X_O': [[3, 4, 5, 7], [7, 1, 35, 1]], 'XXO____XO': [[3, 4, 5, 6], [5, 25, 7, 3]], 'X_OX_____': [[1, 4, 5, 6, 7, 8], [-200, 0, 0, 0, 0, -205]], 'X_OXOX___': [[1, 6, 7, 8], [5, 7, 5, 5]], 'X_OXOX_XO': [[1, 6], [1, 25]], 'X_OXO__X_': [[1, 5, 6, 8], [3, 1, 23, 3]], 'X_OXOO_XX': [[1, 6], [0, 31]], 'X_OXO___X': [[1, 5, 6, 7], [3, 2, 11, 3]], 'X_OXXO___': [[1, 6, 7, 8], [0, 9, 2, 25]], 'X_OXXOOX_': [[1, 8], [0, 23]], 'X_OX_O_X_': [[1, 4, 6, 8], [1, 3, 15, 11]], 'X_OX_O__X': [[1, 4, 6, 7], [2, 2, 7, 2]], 'X_OXX_O__': [[1, 5, 7, 8], [0, 0, 2, 3]], 'X_OXX_OXO': [[1, 5], [3, 21]], 'X_OX_XO__': [[1, 4, 7, 8], [3, 5, 7, 6]], 'X_OX_XOXO': [[1, 4], [0, 235]], 'X_OX__OX_': [[1, 4, 5, 8], [2, 15, 2, 5]], 'X_OX__O_X': [[1, 4, 5, 7], [0, 9, 3, 0]], 'X_OXX__O_': [[1, 5, 6, 8], [0, 1, 1, 3]], 'X_OX_X_O_': [[1, 4, 6, 8], [3, 3, 3, 2]], 'X_OXX___O': [[1, 5, 6, 7], [1, 35, 2, 4]], 'X_OX_X__O': [[1, 4, 6, 7], [-11, 0, 0, -7]], 'X_OX___XO': [[1, 4, 5, 6], [1, 6, 13, 15]], 'X_O_X____': [[1, 3, 5, 6, 7, 8], [0, 16, 0, 0, 0, 33479]], 'X_OOXX___': [[1, 6, 7, 8], [0, 0, 5, 57341]], 'X_OOXXOX_': [[1, 8], [-5, -5]], 'X_OOXX_XO': [[1, 6], [38223, 0]], 'X_OOX__X_': [[1, 5, 6, 8], [10, 0, 0, 1]], 'X_O_XOX__': [[1, 3, 7, 8], [5, 5, 2, 7]], 'X_O_XO_X_': [[1, 3, 6, 8], [0, 3, 0, 43]], 'X_O_XXO__': [[1, 3, 7, 8], [0, 2, 1, 7]], 'X_O_XXOXO': [[1, 3], [-7, -13]], 'X_O_X_OX_': [[1, 3, 5, 8], [-9, 0, 0, -8]], 'X_O_XX_O_': [[1, 3, 6, 8], [3, 4, 3, 4]], 'X_O_XXXOO': [[1, 3], [0, 100]], 'X_O_X_XO_': [[1, 3, 5, 8], [1, 3, 1, 2]], 'X_O_XX__O': [[1, 3, 6, 7], [22, 42677, 0, 10]], 'X_O_X_X_O': [[1, 3, 5, 7], [1, 10, 53, 4]], 'X_O_X__XO': [[1, 3, 5, 6], [48, 1, 113, 0]], 'X_O__X___': [[1, 3, 4, 6, 7, 8], [3, 3, 5, 5, 4, 3]], 'X_OO_X_X_': [[1, 4, 6, 8], [2, 6, 3, 2]], 'X_OOOX_XX': [[1, 6], [2, 31]], 'X_OO_X__X': [[1, 4, 6, 7], [0, 24, 1, 3]], 'X_O_OXX__': [[1, 3, 7, 8], [0, 3584, 8, 0]], 'X_O_OXXXO': [[1, 3], [0, 6305]], 'X_O_OX_X_': [[1, 3, 6, 8], [2, 5, 19, 5]], 'X_O_OX__X': [[1, 3, 6, 7], [15, 54, 45, 65]], 'X_O__XOX_': [[1, 3, 4, 8], [2, 3, 25, 3]], 'X_O__XXO_': [[1, 3, 4, 8], [3, 4, 3, 3]], 'X_O__XX_O': [[1, 3, 4, 7], [1, 562, 0, 0]], 'X_O__X_XO': [[1, 3, 4, 6], [60, 1050, 145, 0]], 'X_O___X__': [[1, 3, 4, 5, 7, 8], [-170, 0, 0, 0, 0, -137]], 'X_O_O_XX_': [[1, 3, 5, 8], [-13, 0, 0, -15]], 'X_O_O_X_X': [[1, 3, 5, 7], [-3, 0, 0, -4]], 'X_O__OXX_': [[1, 3, 4, 8], [3, 1, 3, 15]], 'X_O__OX_X': [[1, 3, 4, 7], [2, 3, 2, 2]], 'X_O___XXO': [[1, 3, 4, 5], [3, 8, 2, 75]], 'X_O____X_': [[1, 3, 4, 5, 6, 8], [0, 1, 1, 2, 0, 1108]], 'X_OO___XX': [[1, 4, 5, 6], [-3, 0, 0, -4]], 'X_O_O__XX': [[1, 3, 5, 6], [1, 2, 3, 21]], 'X_O__O_XX': [[1, 3, 4, 6], [-21, 0, 0, -20]], 'X_O_____X': [[1, 3, 4, 5, 6, 7], [-28, 0, 0, 0, 0, -25]], 'XX_O_____': [[2, 4, 5, 6, 7, 8], [3, 3, 3, 3, 3, 3]], 'XX_OOX___': [[2, 6, 7, 8], [101, 8, 1, 3]], 'XX_OOXOX_': [[2, 8], [27, 2]], 'XX_OOX_XO': [[2, 6], [493, 0]], 'XX_OO__X_': [[2, 5, 6, 8], [16, 11, 2, 3]], 'XX_OO___X': [[2, 5, 6, 7], [11, 27, 1, 1]], 'XX_OXO___': [[2, 6, 7, 8], [2, 2, 2, 2]], 'XX_O_O_X_': [[2, 4, 6, 8], [3, 5, 3, 3]], 'XX_O_O__X': [[2, 4, 6, 7], [2, 3, 5, 3]], 'XX_OX_O__': [[2, 5, 7, 8], [2, 1, 2, 4]], 'XX_OXXOO_': [[2, 8], [1, 21]], 'XX_OXXO_O': [[2, 7], [0, 27]], 'XX_O_XO__': [[2, 4, 7, 8], [9, 8, 3, 2]], 'XX_O_XOXO': [[2, 4], [-45, -41]], 'XX_O__OX_': [[2, 4, 5, 8], [4, 2, 3, 2]], 'XX_OX__O_': [[2, 5, 6, 8], [3, 2, 3, 2]], 'XX_OXX_OO': [[2, 6], [7, 25]], 'XX_O_X_O_': [[2, 4, 6, 8], [4, 3, 2, 2]], 'XX_OX___O': [[2, 5, 6, 7], [3, 3, 3, 4]], 'XX_O_X__O': [[2, 4, 6, 7], [66, 10, 0, 0]], 'XX_O___XO': [[2, 4, 5, 6], [7, 2, 3, 2]], 'X_XO_____': [[1, 4, 5, 6, 7, 8], [3, 3, 3, 3, 3, 3]], 'X_XOOX___': [[1, 6, 7, 8], [-9, 0, 0, -6]], 'X_XOOXOX_': [[1, 8], [-10, -8]], 'X_XOO__X_': [[1, 5, 6, 8], [9, 89, 1, 8]], 'X_XOO___X': [[1, 5, 6, 7], [4, 25, 1, 0]], 'X_XOX_O__': [[1, 5, 7, 8], [2, 2, 4, 3]], 'X_XOXXOO_': [[1, 8], [0, 21]], 'X_XO_XO__': [[1, 4, 7, 8], [3, 0, 2, 15]], 'X_XO__OX_': [[1, 4, 5, 8], [3, 0, 1, 0]], 'X_XOX__O_': [[1, 5, 6, 8], [0, 2, 1, 2]], 'X_XO_X_O_': [[1, 4, 6, 8], [3, 3, 5, 3]], 'X__OX____': [[1, 2, 5, 6, 7, 8], [2, 2, 1, 4, 1, 2]], 'X__OXO_X_': [[1, 2, 6, 8], [3, 2, 2, 5]], 'X__OXXO__': [[1, 2, 7, 8], [0, 0, 0, 30496]], 'X__OXXOXO': [[1, 2], [33133, 0]], 'X__OX_OX_': [[1, 2, 5, 8], [2, 2, 0, 1]], 'X__OXX_O_': [[1, 2, 6, 8], [2, 2, 2, 7]], 'X__OXX__O': [[1, 2, 6, 7], [3679, 8005, 2626, 6322]], 'X__OX__XO': [[1, 2, 5, 6], [5, 1, 2, 2]], 'X__O_X___': [[1, 2, 4, 6, 7, 8], [11, 17, 6, 6, 5, 24]], 'X__OOX_X_': [[1, 2, 6, 8], [2, 457, 2, 40]], 'X__OOX__X': [[1, 2, 6, 7], [0, 341, 0, 0]], 'X__O_XOX_': [[1, 2, 4, 8], [0, 0, 0, 9]], 'X__O_X_XO': [[1, 2, 4, 6], [4, 26, 6, 5]], 'X__O___X_': [[1, 2, 4, 5, 6, 8], [2, 3, 5, 1, 3, 6]], 'X__OO__XX': [[1, 2, 5, 6], [3, 3, 23, 13]], 'X__O____X': [[1, 2, 4, 5, 6, 7], [0, 0, 12, 7, 1, 0]], 'XX__O____': [[2, 3, 5, 6, 7, 8], [184469, 0, 0, 0, 0, 0]], 'XX_XOO___': [[2, 6, 7, 8], [-35, 0, 0, -28]], 'XX_XOOOX_': [[2, 8], [31, 0]], 'XX_XOO_XO': [[2, 6], [21, 0]], 'XX__OOX__': [[2, 3, 7, 8], [3, 39, 1, 1]], 'XX__OOXXO': [[2, 3], [13, 11]], 'XX__OO_X_': [[2, 3, 6, 8], [5, 19, 2, 7]], 'XX_XO_O__': [[2, 5, 7, 8], [13, 3, 10, 4]], 'XX_XOXOO_': [[2, 8], [9, 13]], 'XX_XOXO_O': [[2, 7], [27, 41]], 'XX_XO_OXO': [[2, 5], [23, 1]], 'XX__OXO__': [[2, 3, 7, 8], [27, 3, 1, 2]], 'XX__OXOXO': [[2, 3], [43, 1]], 'XX__O_OX_': [[2, 3, 5, 8], [127, 1, 4, 0]], 'XX_XO__O_': [[2, 5, 6, 8], [-2, 0, 0, -3]], 'XX_XOX_OO': [[2, 6], [1, 19]], 'XX__OX_O_': [[2, 3, 6, 8], [15704, 4, 0, 0]], 'XX_XO___O': [[2, 5, 6, 7], [-6, 0, 0, -8]], 'XX__OX__O': [[2, 3, 6, 7], [7190, 4, 0, 0]], 'XX__O_X_O': [[2, 3, 5, 7], [-9, 0, 0, -9]], 'XX__O__XO': [[2, 3, 5, 6], [22, 1, 1, 5]], 'X_X_O____': [[1, 3, 5, 6, 7, 8], [213804, 0, 0, 0, 0, 0]], 'X_XXO_O__': [[1, 5, 7, 8], [150325, 5, 0, 0]], 'X_X_O_OX_': [[1, 3, 5, 8], [7093, 0, 0, 0]], 'X_XXO__O_': [[1, 5, 6, 8], [21, 1, 2, 2]], 'X__XO____': [[1, 2, 5, 6, 7, 8], [1, 0, 0, 150476, 0, 0]], 'X__XOO_X_': [[1, 2, 6, 8], [1, 5, 92, 0]], 'X__XOXO__': [[1, 2, 7, 8], [6, 11, 5, 15]], 'X__XOXOXO': [[1, 2], [39, 105]], 'X__XO_OX_': [[1, 2, 5, 8], [12, 35, 11, 8]], 'X__XOX_O_': [[1, 2, 6, 8], [3, 2, 15, 7]], 'X__XOX__O': [[1, 2, 6, 7], [3, 1, 34, 8]], 'X__XO__XO': [[1, 2, 5, 6], [0, 0, 0, 420]], 'X___OX___': [[1, 2, 3, 6, 7, 8], [7115, 3659, 8, 1, 15714, 11574]], 'X___OXOX_': [[1, 2, 3, 8], [4, 33, 4, 4]], 'X___OX_XO': [[1, 2, 3, 6], [1594, 5584, 727, 5355]], 'X___O__X_': [[1, 2, 3, 5, 6, 8], [256, 0, 500, 85, 2653, 30]], 'X___O___X': [[1, 2, 3, 5, 6, 7], [3348, 0, 325, 38, 0, 1742]], 'XX___O___': [[2, 3, 4, 6, 7, 8], [3, 2, 12, 2, 4, 4]], 'XX_X_OO__': [[2, 4, 7, 8], [7, 2, 1, 1]], 'XX_XXOOO_': [[2, 8], [0, 25]], 'XX_XXOO_O': [[2, 7], [9, 29]], 'XX_X_OOXO': [[2, 4], [25, 0]], 'XX__XOO__': [[2, 3, 7, 8], [3, 0, 2, 1]], 'XX___OOX_': [[2, 3, 4, 8], [2, 1, 6, 3]], 'XX_X_O_O_': [[2, 4, 6, 8], [2, 2, 3, 3]], 'XX_XXO_OO': [[2, 6], [7, 9]], 'XX__XO_O_': [[2, 3, 6, 8], [2, 2, 4, 5]], 'XX_X_O__O': [[2, 4, 6, 7], [9, 1, 7, 3]], 'XX__XO__O': [[2, 3, 6, 7], [23, 2, 1, 6]], 'XX___OX_O': [[2, 3, 4, 7], [7, 5, 4, 1]], 'XX___O_XO': [[2, 3, 4, 6], [9, 3, 2, 2]], 'X__X_O___': [[1, 2, 4, 6, 7, 8], [0, 0, 1, 46, 0, 0]], 'X__XXOO__': [[1, 2, 7, 8], [5, 3, 1, 55]], 'X__XXOOXO': [[1, 2], [8, 47]], 'X__X_OOX_': [[1, 2, 4, 8], [4, 16, 4, 5]], 'X__XXO_O_': [[1, 2, 6, 8], [3, 3, 4, 3]], 'X__XXO__O': [[1, 2, 6, 7], [2, 7, 16, 9]], 'X__X_O_XO': [[1, 2, 4, 6], [2, 15, 1, 6]], 'X___XO___': [[1, 2, 3, 6, 7, 8], [3, 2, 5, 2, 1, 5]], 'X___XOOX_': [[1, 2, 3, 8], [2, 2, 1, 5]], 'X___XOX_O': [[1, 2, 3, 7], [3, 15, 4, 2]], 'X___XO_XO': [[1, 2, 3, 6], [3, 17, 3, 0]], 'X____OX__': [[1, 2, 3, 4, 7, 8], [1, 1, 4, 1, 0, 2]], 'X____OXXO': [[1, 2, 3, 4], [5, 3, 5, 4]], 'X____O_X_': [[1, 2, 3, 4, 6, 8], [3, 5, 5, 3, 3, 3]], 'XX____O__': [[2, 3, 4, 5, 7, 8], [-550, 0, 0, 0, 0, -570]], 'XX_X__OO_': [[2, 4, 5, 8], [7, 4, 2, 5]], 'XX__X_OO_': [[2, 3, 5, 8], [2, 3, 0, 37]], 'XX___XOO_': [[2, 3, 4, 8], [13, 4, 4, 9]], 'XX_X__O_O': [[2, 4, 5, 7], [19, 3, 5, 9]], 'XX__X_O_O': [[2, 3, 5, 7], [4, 2, 0, 37]], 'XX___XO_O': [[2, 3, 4, 7], [14, 1, 2, 25]], 'XX____OXO': [[2, 3, 4, 5], [-101, 0, 0, -94]], 'X_X___O__': [[1, 3, 4, 5, 7, 8], [-55, 0, 0, 0, 0, -41]], 'X__X__O__': [[1, 2, 4, 5, 7, 8], [6, 3, 5, 2, 5, 4]], 'X__XX_OO_': [[1, 2, 5, 8], [3, 1, 5, 7]], 'X__X_XOO_': [[1, 2, 4, 8], [4, 2, 3, 9]], 'X__XX_O_O': [[1, 2, 5, 7], [2, 1, 12, 53]], 'X__X_XO_O': [[1, 2, 4, 7], [9, 0, 53, 47]], 'X__X__OXO': [[1, 2, 4, 5], [73, 411, 183, 46]], 'X___X_O__': [[1, 2, 3, 5, 7, 8], [0, 0, 0, 0, 4, 57031]], 'X___XXOO_': [[1, 2, 3, 8], [2, 1, 2, 27]], 'X___XXO_O': [[1, 2, 3, 7], [2, 0, 22, 47]], 'X___X_OXO': [[1, 2, 3, 5], [92455, 0, 0, 0]], 'X____XO__': [[1, 2, 3, 4, 7, 8], [0, 24, 15, 5, 17, 190]], 'X____XOXO': [[1, 2, 3, 4], [339, 0, 0, 267]], 'X_____OX_': [[1, 2, 3, 4, 5, 8], [774, 0, 0, 425, 1, 105]], 'XX_____O_': [[2, 3, 4, 5, 6, 8], [35, 0, 1, 0, 1, 2]], 'XX_X___OO': [[2, 4, 5, 6], [3, 2, 1, 19]], 'XX__X__OO': [[2, 3, 5, 6], [35, 5, 4, 9]], 'XX___X_OO': [[2, 3, 4, 6], [17, 3, 0, 15]], 'X__X___O_': [[1, 2, 4, 5, 6, 8], [3, 3, 3, 3, 3, 4]], 'X__XX__OO': [[1, 2, 5, 6], [0, 4, 3, 11]], 'X__X_X_OO': [[1, 2, 4, 6], [2, 2, 2, 17]], 'X___X__O_': [[1, 2, 3, 5, 6, 8], [2, 3, 3, 4, 5, 3]], 'X___XX_OO': [[1, 2, 3, 6], [1, 2, 5, 5]], 'X____X_O_': [[1, 2, 3, 4, 6, 8], [2, 5, 2, 2, 5, 7]], 'XX______O': [[2, 3, 4, 5, 6, 7], [292, 0, 0, 0, 5, 1]], 'X__X____O': [[1, 2, 4, 5, 6, 7], [0, 0, 0, 4, 746, 9]], 'X___X___O': [[1, 2, 3, 5, 6, 7], [34, 9221, 0, 5, 35339, 0]], 'X____X__O': [[1, 2, 3, 4, 6, 7], [15, 603, 0, 825, 434, 4]], 'X______XO': [[1, 2, 3, 4, 5, 6], [5, 12, 9, 4, 14, 2]], '_X_______': [[0, 2, 3, 4, 5, 6, 7, 8], [0, 6459, 0, 89821, 17, 2079, 266, 485]], 'OX_X_____': [[2, 4, 5, 6, 7, 8], [6, 15, 83, 22, 26, 20]], 'OXOXX____': [[5, 6, 7, 8], [-3, 0, 0, -2]], 'OXOX_X___': [[4, 6, 7, 8], [31, 3, 1, 3]], 'OXOXOX_X_': [[6, 8], [5, 33]], 'OXOX_XOX_': [[4, 8], [9, 0]], 'OXOX___X_': [[4, 5, 6, 8], [49, 0, 0, 0]], 'OX_XOX___': [[2, 6, 7, 8], [32, 6, 9, 11]], 'OX_XO__X_': [[2, 5, 6, 8], [5, 7, 8, 13]], 'OX_XXO___': [[2, 6, 7, 8], [0, 14, 12747, 0]], 'OX_X_O_X_': [[2, 4, 6, 8], [2, 7, 5, 6]], 'OX_XX_O__': [[2, 5, 7, 8], [-12, 0, 0, -9]], 'OX_X_XO__': [[2, 4, 7, 8], [2, 9, 2, 4]], 'OX_XX__O_': [[2, 5, 6, 8], [13, 29083, 0, 0]], 'OX_X_X_O_': [[2, 4, 6, 8], [3, 5, 3, 5]], 'OX_XX___O': [[2, 5, 6, 7], [2, 1, 0, 1]], 'OX_X_X__O': [[2, 4, 6, 7], [0, 17, 2, 1]], 'OX_X___XO': [[2, 4, 5, 6], [3, 15, 3, 6]], 'OX__X____': [[2, 3, 5, 6, 7, 8], [0, 0, 0, 0, 97818, 0]], 'OX_OXX___': [[2, 6, 7, 8], [2, 9, 2, 3]], 'OX__XXO__': [[2, 3, 7, 8], [1, 13, 8, 3]], 'OX__XX_O_': [[2, 3, 6, 8], [0, 4191, 0, 0]], 'OX__XX__O': [[2, 3, 6, 7], [-1, 0, 0, -1]], 'OX___X___': [[2, 3, 4, 6, 7, 8], [3, 3, 3, 7, 3, 5]], 'OX_O_X_X_': [[2, 4, 6, 8], [3, 4, 7, 3]], 'OX__OX_X_': [[2, 3, 6, 8], [3, 12, 5, 9]], 'OX___XOX_': [[2, 3, 4, 8], [2, 109, 87, 7]], 'OX_____X_': [[2, 3, 4, 5, 6, 8], [3, 4, 31, 1, 11, 12]], '_XOX_____': [[0, 4, 5, 6, 7, 8], [27, 1390, 37, 7, 198, 409]], '_XOXO__X_': [[0, 5, 6, 8], [2, 7, 15, 7]], '_XOXXO___': [[0, 6, 7, 8], [3, 4, 5, 15]], '_XOX_O_X_': [[0, 4, 6, 8], [2, 7, 2, 9]], '_XOXX__O_': [[0, 5, 6, 8], [6, 22495, 0, 0]], '_XOXX___O': [[0, 5, 6, 7], [0, 23, 2, 5]], '_XO_X____': [[0, 3, 5, 6, 7, 8], [45, 0, 0, 0, 90227, 6]], '_XO____X_': [[0, 3, 4, 5, 6, 8], [0, 8, 117, 9, 1, 0]], '_X_OX____': [[0, 2, 5, 6, 7, 8], [7, 1, 2, 1, 5, 0]], '_X_OXXO__': [[0, 2, 7, 8], [25, 0, 3, 2]], '_X_OXX_O_': [[0, 2, 6, 8], [9, 4, 5, 6]], '_X_O_X___': [[0, 2, 4, 6, 7, 8], [2, 3, 5, 8, 3, 5]], '_X_OOX_X_': [[0, 2, 6, 8], [4, 58, 2, 17]], '_X_O___X_': [[0, 2, 4, 5, 6, 8], [1, 1, 6, 5, 1, 3]], '_X_XO____': [[0, 2, 5, 6, 7, 8], [8685, 3591, 120, 443, 253, 12]], '_X__O__X_': [[0, 2, 3, 5, 6, 8], [12, 18, 3, 40, 71, 0]], '_X_X_O___': [[0, 2, 4, 6, 7, 8], [5, 2, 4, 2, 5, 13]], '_X_XXO__O': [[0, 2, 6, 7], [3, 13, 2, 17]], '_X__XO___': [[0, 2, 3, 6, 7, 8], [1, 0, 0, 2, 1, 2]], '_X__X_O__': [[0, 2, 3, 5, 7, 8], [0, 0, 0, 0, 18790, 0]], '_X___XO__': [[0, 2, 3, 4, 7, 8], [3, 5, 9, 5, 5, 3]], '_X__X__O_': [[0, 2, 3, 5, 6, 8], [20, 33, 12, 7, 22, 10]], '_X__X___O': [[0, 2, 3, 5, 6, 7], [0, 2, 0, 1, 0, 30546]], '____X____': [[0, 1, 2, 3, 5, 6, 7, 8], [0, 0, 0, 0, 0, 369245, 0, 0]]}