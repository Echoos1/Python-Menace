class Dictionary:
	states = {'_________': [[0, 1, 2, 3, 4, 5, 6, 7, 8], [2736, 2003, 93, 468, 2640, 1283, 4445, 993, 370]], 'XO_______': [[2, 3, 4, 5, 6, 7, 8], [11, 120, 251, 218, 231, 90, 41]], 'XOXO_____': [[4, 5, 6, 7, 8], [44, 5, 21, 2, 11]], 'XOXOXO___': [[6, 7, 8], [15, 27, 41]], 'XOXOXOOX_': [[8], [147]], 'XOXOXO_XO': [[6], [119]], 'XOXOX_O__': [[5, 7, 8], [23, 20, 63]], 'XOXOXXOO_': [[8], [109]], 'XOXOXXO_O': [[7], [41]], 'XOXOX_OXO': [[5], [62]], 'XOXOX__O_': [[5, 6, 8], [13, 45, 57]], 'XOXOXX_OO': [[6], [91]], 'XOXOX___O': [[5, 6, 7], [11, 107, 9]], 'XOXOOX___': [[6, 7, 8], [1, 57, 17]], 'XOXOOXX_O': [[7], [44]], 'XOXOOXOX_': [[8], [155]], 'XOXOOX_XO': [[6], [73]], 'XOXO_XO__': [[4, 7, 8], [4, 13, 11]], 'XOXO_XOXO': [[4], [30]], 'XOXO_X_O_': [[4, 6, 8], [13, 6, 11]], 'XOXO_XXOO': [[4], [139]], 'XOXO_X__O': [[4, 6, 7], [6, 17, 4]], 'XOXOO_X__': [[5, 7, 8], [6, 1, 0]], 'XOXOO_XXO': [[5], [49]], 'XOXO_OX__': [[4, 7, 8], [21, 3, 1]], 'XOXO_OXXO': [[4], [103]], 'XOXO_OXOX': [[4], [11]], 'XOXO__XO_': [[4, 5, 8], [29, 16, 1]], 'XOXO__X_O': [[4, 5, 7], [29, 8, 12]], 'XOXOO__X_': [[5, 6, 8], [8, 2, 3]], 'XOXOO_OXX': [[5], [97]], 'XOXO_O_X_': [[4, 6, 8], [7, 8, 5]], 'XOXO__OX_': [[4, 5, 8], [10, 10, 21]], 'XOXO___XO': [[4, 5, 6], [3, 3, 19]], 'XOXOO___X': [[5, 6, 7], [45, 1, 2]], 'XOXO__O_X': [[4, 5, 7], [9, 37, 53]], 'XOXO___OX': [[4, 5, 6], [9, 15, 8]], 'XOX_O____': [[3, 5, 6, 7, 8], [33, 19, 4, 6, 2]], 'XOXXOO___': [[6, 7, 8], [39, 47, 1]], 'XOXXOOOX_': [[8], [66]], 'XOXXOO_XO': [[6], [189]], 'XOXXO_O__': [[5, 7, 8], [4, 28, 5]], 'XOXXOXO_O': [[7], [43]], 'XOXXO_OXO': [[5], [91]], 'XOXXO___O': [[5, 6, 7], [6, 25, 34]], 'XOX_OXO__': [[3, 7, 8], [3, 6, 55]], 'XOX_OXOXO': [[3], [53]], 'XOX_OX__O': [[3, 6, 7], [6, 1, 5]], 'XOX_OOX__': [[3, 7, 8], [15, 6, 1]], 'XOX_OOXXO': [[3], [109]], 'XOX_O_X_O': [[3, 5, 7], [49, 0, 13]], 'XOX_OO_X_': [[3, 6, 8], [9, 3, 3]], 'XOX_O_OX_': [[3, 5, 8], [9, 5, 18]], 'XOX_O__XO': [[3, 5, 6], [21, 5, 13]], 'XOX_O_O_X': [[3, 5, 7], [8, 29, 16]], 'XOX__O___': [[3, 4, 6, 7, 8], [9, 53, 2, 19, 15]], 'XOXX_OO__': [[4, 7, 8], [16, 8, 15]], 'XOXXXOOO_': [[8], [203]], 'XOXXXOO_O': [[7], [74]], 'XOXX_OOXO': [[4], [70]], 'XOXX_O_O_': [[4, 6, 8], [21, 47, 0]], 'XOXXXO_OO': [[6], [137]], 'XOXX_O__O': [[4, 6, 7], [39, 23, 11]], 'XOX_XOO__': [[3, 7, 8], [40, 14, 21]], 'XOX_XOOXO': [[3], [80]], 'XOX_XO_O_': [[3, 6, 8], [31, 81, 21]], 'XOX_XO__O': [[3, 6, 7], [9, 67, 13]], 'XOX__OXO_': [[3, 4, 8], [5, 45, 0]], 'XOX__OX_O': [[3, 4, 7], [5, 3, 45]], 'XOX__OOX_': [[3, 4, 8], [14, 5, 18]], 'XOX__O_XO': [[3, 4, 6], [13, 6, 29]], 'XOX___O__': [[3, 4, 5, 7, 8], [18, 43, 14, 21, 24]], 'XOXX__OO_': [[4, 5, 8], [14, 1, 3]], 'XOXX__O_O': [[4, 5, 7], [2, 5, 11]], 'XOX_X_OO_': [[3, 5, 8], [31, 3, 19]], 'XOX_X_O_O': [[3, 5, 7], [2, 4, 21]], 'XOX__XOO_': [[3, 4, 8], [1, 1, 25]], 'XOX__XO_O': [[3, 4, 7], [4, 3, 18]], 'XOX___OXO': [[3, 4, 5], [11, 16, 7]], 'XOX___OOX': [[3, 4, 5], [2, 23, 15]], 'XOX____O_': [[3, 4, 5, 6, 8], [20, 66, 11, 4, 4]], 'XOXX___OO': [[4, 5, 6], [11, 1, 29]], 'XOX_X__OO': [[3, 5, 6], [5, 1, 39]], 'XOX__X_OO': [[3, 4, 6], [1, 12, 15]], 'XOX___XOO': [[3, 4, 5], [73, 7, 5]], 'XOX_____O': [[3, 4, 5, 6, 7], [21, 5, 14, 6, 12]], 'XOOX_____': [[4, 5, 6, 7, 8], [26, 1, 91, 4, 32]], 'XOOXXO___': [[6, 7, 8], [61, 1, 23]], 'XOOXXOOX_': [[8], [81]], 'XOOXX_O__': [[5, 7, 8], [13, 33, 25]], 'XOOXX_OXO': [[5], [109]], 'XOOXX__O_': [[5, 6, 8], [25, 91, 5]], 'XOOXX___O': [[5, 6, 7], [57, 17, 1]], 'XOOXOX___': [[6, 7, 8], [7, 5, 1]], 'XOOXOX_XO': [[6], [97]], 'XOOX_XO__': [[4, 7, 8], [3, 6, 5]], 'XOOX_XOXO': [[4], [89]], 'XOOX_XOOX': [[4], [27]], 'XOOX_X_O_': [[4, 6, 8], [9, 25, 1]], 'XOOX_X__O': [[4, 6, 7], [19, 9, 9]], 'XOOXO__X_': [[5, 6, 8], [7, 5, 6]], 'XOOXOO_XX': [[6], [69]], 'XOOX_O_X_': [[4, 6, 8], [1, 15, 13]], 'XOOX_OOXX': [[4], [67]], 'XOOX__OX_': [[4, 5, 8], [13, 3, 3]], 'XOOX___XO': [[4, 5, 6], [4, 13, 5]], 'XOOXO___X': [[5, 6, 7], [2, 29, 6]], 'XOOX_O__X': [[4, 6, 7], [17, 13, 5]], 'XOOX__O_X': [[4, 5, 7], [23, 2, 14]], 'XOOX___OX': [[4, 5, 6], [11, 2, 13]], 'XO_XO____': [[2, 5, 6, 7, 8], [22, 4, 13, 13, 5]], 'XO_XOXO__': [[2, 7, 8], [3, 2, 2]], 'XO_XOXOXO': [[2], [42]], 'XO_XOX__O': [[2, 6, 7], [3, 27, 21]], 'XO_XOO_X_': [[2, 6, 8], [17, 7, 20]], 'XO_XOOOXX': [[2], [33]], 'XO_XO_OX_': [[2, 5, 8], [12, 2, 0]], 'XO_XO__XO': [[2, 5, 6], [19, 16, 13]], 'XO_XOO__X': [[2, 6, 7], [2, 17, 9]], 'XO_XO_O_X': [[2, 5, 7], [2, 0, 2]], 'XO_X_O___': [[2, 4, 6, 7, 8], [76, 52, 19, 26, 8]], 'XO_XXOO__': [[2, 7, 8], [30, 6, 53]], 'XO_XXOOXO': [[2], [33]], 'XO_XXO_O_': [[2, 6, 8], [25, 7, 41]], 'XO_XXO__O': [[2, 6, 7], [55, 13, 2]], 'XO_X_OOX_': [[2, 4, 8], [5, 12, 23]], 'XO_X_O_XO': [[2, 4, 6], [19, 3, 13]], 'XO_X_OO_X': [[2, 4, 7], [20, 29, 6]], 'XO_X_O_OX': [[2, 4, 6], [5, 23, 19]], 'XO_X__O__': [[2, 4, 5, 7, 8], [4, 32, 5, 11, 9]], 'XO_XX_OO_': [[2, 5, 8], [8, 67, 23]], 'XO_XX_O_O': [[2, 5, 7], [4, 39, 18]], 'XO_X_XOO_': [[2, 4, 8], [2, 11, 6]], 'XO_X_XO_O': [[2, 4, 7], [2, 7, 7]], 'XO_X__OXO': [[2, 4, 5], [4, 7, 25]], 'XO_X__OOX': [[2, 4, 5], [1, 33, 1]], 'XO_X___O_': [[2, 4, 5, 6, 8], [6, 65, 4, 5, 6]], 'XO_XX__OO': [[2, 5, 6], [2, 27, 35]], 'XO_X_X_OO': [[2, 4, 6], [0, 3, 25]], 'XO_X____O': [[2, 4, 5, 6, 7], [18, 21, 36, 33, 16]], 'XOO_X____': [[3, 5, 6, 7, 8], [65, 48, 44, 6, 17]], 'XOOOXX___': [[6, 7, 8], [10, 24, 31]], 'XOOOXXOX_': [[8], [141]], 'XOOOXX_XO': [[6], [72]], 'XOO_XXO__': [[3, 7, 8], [35, 41, 13]], 'XOO_XXOXO': [[3], [245]], 'XOO_XX_O_': [[3, 6, 8], [9, 49, 5]], 'XOO_XXXOO': [[3], [113]], 'XOO_XX__O': [[3, 6, 7], [45, 8, 37]], 'XOO_XOX__': [[3, 7, 8], [21, 6, 65]], 'XOO_X_XO_': [[3, 5, 8], [43, 9, 61]], 'XOO_X_X_O': [[3, 5, 7], [71, 7, 0]], 'XOOOX__X_': [[5, 6, 8], [11, 8, 3]], 'XOO_XO_X_': [[3, 6, 8], [3, 1, 37]], 'XOO_X_OX_': [[3, 5, 8], [19, 29, 29]], 'XOO_X__XO': [[3, 5, 6], [7, 19, 3]], 'XO_OX____': [[2, 5, 6, 7, 8], [38, 76, 87, 5, 23]], 'XO_OXXO__': [[2, 7, 8], [27, 18, 29]], 'XO_OXXOXO': [[2], [74]], 'XO_OXX_O_': [[2, 6, 8], [49, 37, 3]], 'XO_OXX__O': [[2, 6, 7], [7, 26, 13]], 'XO_OXO_X_': [[2, 6, 8], [15, 23, 33]], 'XO_OX_OX_': [[2, 5, 8], [11, 15, 17]], 'XO_OX__XO': [[2, 5, 6], [3, 12, 14]], 'XO__XO___': [[2, 3, 6, 7, 8], [25, 14, 3, 56, 41]], 'XO__XOXO_': [[2, 3, 8], [5, 87, 25]], 'XO__XOX_O': [[2, 3, 7], [17, 55, 1]], 'XO__XOOX_': [[2, 3, 8], [37, 12, 29]], 'XO__XO_XO': [[2, 3, 6], [35, 1, 9]], 'XO__X_O__': [[2, 3, 5, 7, 8], [17, 27, 69, 3, 7]], 'XO__XXOO_': [[2, 3, 8], [5, 25, 47]], 'XO__XXO_O': [[2, 3, 7], [1, 43, 21]], 'XO__X_OXO': [[2, 3, 5], [9, 13, 27]], 'XO__X__O_': [[2, 3, 5, 6, 8], [43, 21, 67, 9, 7]], 'XO__XX_OO': [[2, 3, 6], [2, 7, 47]], 'XO__X_XOO': [[2, 3, 5], [5, 63, 21]], 'XO__X___O': [[2, 3, 5, 6, 7], [13, 41, 28, 13, 11]], 'XOO__X___': [[3, 4, 6, 7, 8], [22, 15, 46, 3, 22]], 'XOO_OXX__': [[3, 7, 8], [43, 43, 4]], 'XOO_OXXXO': [[3], [179]], 'XOO__XXO_': [[3, 4, 8], [47, 7, 1]], 'XOO__XX_O': [[3, 4, 7], [3, 17, 40]], 'XOOO_X_X_': [[4, 6, 8], [7, 6, 25]], 'XOOOOX_XX': [[6], [131]], 'XOOO_XOXX': [[4], [93]], 'XOO_OX_X_': [[3, 6, 8], [2, 43, 4]], 'XOO__XOX_': [[3, 4, 8], [3, 27, 2]], 'XOO__X_XO': [[3, 4, 6], [25, 40, 15]], 'XOOO_X__X': [[4, 6, 7], [35, 17, 15]], 'XOO_OX__X': [[3, 6, 7], [1, 1, 9]], 'XOO__XO_X': [[3, 4, 7], [13, 3, 6]], 'XO_O_X___': [[2, 4, 6, 7, 8], [13, 5, 7, 50, 38]], 'XO_OOX_X_': [[2, 6, 8], [28, 10, 37]], 'XO_OOXOXX': [[2], [95]], 'XO_O_XOX_': [[2, 4, 8], [5, 15, 19]], 'XO_O_X_XO': [[2, 4, 6], [11, 14, 10]], 'XO_OOX__X': [[2, 6, 7], [33, 2, 5]], 'XO_O_XO_X': [[2, 4, 7], [7, 17, 19]], 'XO__OX___': [[2, 3, 6, 7, 8], [5, 16, 18, 28, 1]], 'XO__OXX_O': [[2, 3, 7], [7, 13, 28]], 'XO__OXOX_': [[2, 3, 8], [32, 2, 1]], 'XO__OX_XO': [[2, 3, 6], [17, 26, 6]], 'XO__OXO_X': [[2, 3, 7], [13, 1, 1]], 'XO___XO__': [[2, 3, 4, 7, 8], [23, 4, 15, 16, 3]], 'XO___XOXO': [[2, 3, 4], [4, 23, 15]], 'XO___X_O_': [[2, 3, 4, 6, 8], [8, 10, 35, 13, 2]], 'XO___XXOO': [[2, 3, 4], [3, 47, 5]], 'XO___X__O': [[2, 3, 4, 6, 7], [10, 9, 25, 19, 21]], 'XOO___X__': [[3, 4, 5, 7, 8], [7, 18, 17, 54, 15]], 'XOO_O_XX_': [[3, 5, 8], [19, 23, 25]], 'XOO__OXX_': [[3, 4, 8], [27, 5, 13]], 'XOO___XXO': [[3, 4, 5], [57, 1, 11]], 'XOO_O_X_X': [[3, 5, 7], [39, 1, 21]], 'XOO__OX_X': [[3, 4, 7], [9, 9, 79]], 'XO__O_X__': [[2, 3, 5, 7, 8], [2, 127, 7, 20, 7]], 'XO__OOXX_': [[2, 3, 8], [1, 19, 29]], 'XO__O_XXO': [[2, 3, 5], [9, 29, 9]], 'XO__OOX_X': [[2, 3, 7], [1, 23, 33]], 'XO___OX__': [[2, 3, 4, 7, 8], [21, 15, 130, 12, 27]], 'XO___OXXO': [[2, 3, 4], [23, 7, 3]], 'XO____XO_': [[2, 3, 4, 5, 8], [7, 9, 59, 14, 11]], 'XO____X_O': [[2, 3, 4, 5, 7], [11, 109, 18, 26, 14]], 'XOO____X_': [[3, 4, 5, 6, 8], [3, 10, 19, 30, 18]], 'XOOO___XX': [[4, 5, 6], [11, 43, 13]], 'XOO_O__XX': [[3, 5, 6], [2, 5, 25]], 'XOO__O_XX': [[3, 4, 6], [9, 21, 13]], 'XOO___OXX': [[3, 4, 5], [4, 27, 2]], 'XO_O___X_': [[2, 4, 5, 6, 8], [8, 8, 14, 11, 72]], 'XO_OO__XX': [[2, 5, 6], [4, 39, 5]], 'XO_O_O_XX': [[2, 4, 6], [3, 5, 27]], 'XO_O__OXX': [[2, 4, 5], [17, 19, 9]], 'XO__O__X_': [[2, 3, 5, 6, 8], [9, 11, 39, 26, 5]], 'XO__OO_XX': [[2, 3, 6], [3, 6, 7]], 'XO__O_OXX': [[2, 3, 5], [5, 3, 5]], 'XO___O_X_': [[2, 3, 4, 6, 8], [13, 6, 7, 19, 16]], 'XO___OOXX': [[2, 3, 4], [10, 3, 23]], 'XO____OX_': [[2, 3, 4, 5, 8], [15, 9, 42, 17, 13]], 'XO_____XO': [[2, 3, 4, 5, 6], [3, 32, 32, 25, 21]], 'XOO_____X': [[3, 4, 5, 6, 7], [13, 19, 22, 10, 20]], 'XO_O____X': [[2, 4, 5, 6, 7], [30, 27, 25, 11, 15]], 'XO__O___X': [[2, 3, 5, 6, 7], [3, 4, 3, 6, 2]], 'XO___O__X': [[2, 3, 4, 6, 7], [6, 34, 59, 1, 6]], 'XO____O_X': [[2, 3, 4, 5, 7], [19, 28, 37, 3, 10]], 'XO_____OX': [[2, 3, 4, 5, 6], [5, 4, 5, 2, 5]], 'X_O______': [[1, 3, 4, 5, 6, 7, 8], [23, 140, 360, 72, 206, 25, 187]], 'XXOO_____': [[4, 5, 6, 7, 8], [4, 16, 5, 21, 13]], 'XXOOXO___': [[6, 7, 8], [12, 35, 23]], 'XXOOX_O__': [[5, 7, 8], [31, 35, 61]], 'XXOOXXOO_': [[8], [123]], 'XXOOXXO_O': [[7], [121]], 'XXOOX__O_': [[5, 6, 8], [8, 9, 33]], 'XXOOXX_OO': [[6], [65]], 'XXOOX___O': [[5, 6, 7], [36, 1, 3]], 'XXOOOX___': [[6, 7, 8], [9, 1, 4]], 'XXOOOX_XO': [[6], [28]], 'XXOO_XO__': [[4, 7, 8], [15, 3, 2]], 'XXOO_XOXO': [[4], [71]], 'XXOO_X_O_': [[4, 6, 8], [23, 3, 11]], 'XXOO_X__O': [[4, 6, 7], [13, 3, 11]], 'XXOOO__X_': [[5, 6, 8], [5, 2, 2]], 'XXOO_O_X_': [[4, 6, 8], [3, 2, 9]], 'XXOO_OOXX': [[4], [17]], 'XXOO__OX_': [[4, 5, 8], [21, 2, 3]], 'XXOO___XO': [[4, 5, 6], [13, 12, 4]], 'XXOOO___X': [[5, 6, 7], [4, 3, 0]], 'XXOO_O__X': [[4, 6, 7], [17, 5, 1]], 'XXOO__O_X': [[4, 5, 7], [41, 1, 3]], 'XXO_O____': [[3, 5, 6, 7, 8], [1, 4, 10, 1, 2]], 'XXOXOO___': [[6, 7, 8], [11, 2, 6]], 'XXOXO__O_': [[5, 6, 8], [3, 13, 13]], 'XXOXOX_OO': [[6], [37]], 'XXOXO___O': [[5, 6, 7], [3, 13, 1]], 'XXO_OX_O_': [[3, 6, 8], [4, 10, 2]], 'XXO_OXXOO': [[3], [157]], 'XXO_OX__O': [[3, 6, 7], [4, 6, 3]], 'XXO_OOX__': [[3, 7, 8], [55, 2, 3]], 'XXO_O_XO_': [[3, 5, 8], [37, 24, 8]], 'XXO_O_X_O': [[3, 5, 7], [25, 25, 3]], 'XXO_OO_X_': [[3, 6, 8], [2, 1, 2]], 'XXO_O__XO': [[3, 5, 6], [2, 2, 5]], 'XXO_OO__X': [[3, 6, 7], [5, 8, 1]], 'XXO__O___': [[3, 4, 6, 7, 8], [9, 8, 2, 3, 5]], 'XXOX_OO__': [[4, 7, 8], [6, 2, 5]], 'XXOXXOOO_': [[8], [113]], 'XXOX_O_O_': [[4, 6, 8], [2, 9, 9]], 'XXO_XOO__': [[3, 7, 8], [18, 37, 5]], 'XXO_XO_O_': [[3, 6, 8], [4, 0, 13]], 'XXO__OXO_': [[3, 4, 8], [7, 3, 19]], 'XXO__OOX_': [[3, 4, 8], [2, 9, 4]], 'XXO__OO_X': [[3, 4, 7], [12, 7, 1]], 'XXO___O__': [[3, 4, 5, 7, 8], [1, 12, 3, 1, 15]], 'XXOX__OO_': [[4, 5, 8], [8, 0, 1]], 'XXOX__O_O': [[4, 5, 7], [2, 2, 1]], 'XXO_X_OO_': [[3, 5, 8], [16, 5, 9]], 'XXO_X_O_O': [[3, 5, 7], [1, 2, 43]], 'XXO__XOO_': [[3, 4, 8], [3, 4, 9]], 'XXO__XO_O': [[3, 4, 7], [1, 10, 4]], 'XXO___OXO': [[3, 4, 5], [2, 13, 3]], 'XXO____O_': [[3, 4, 5, 6, 8], [9, 3, 3, 5, 18]], 'XXOX___OO': [[4, 5, 6], [2, 2, 3]], 'XXO_X__OO': [[3, 5, 6], [1, 3, 8]], 'XXO__X_OO': [[3, 4, 6], [2, 2, 3]], 'XXO___XOO': [[3, 4, 5], [13, 2, 5]], 'XXO_____O': [[3, 4, 5, 6, 7], [2, 5, 4, 3, 2]], 'X_OXO____': [[1, 5, 6, 7, 8], [11, 1, 91, 0, 22]], 'X_OXOX_O_': [[1, 6, 8], [3, 13, 1]], 'X_OXOX__O': [[1, 6, 7], [1, 23, 0]], 'X_OXOO_X_': [[1, 6, 8], [2, 25, 2]], 'X_OXO__XO': [[1, 5, 6], [0, 15, 19]], 'X_OXOO__X': [[1, 6, 7], [5, 33, 6]], 'X_OX_O___': [[1, 4, 6, 7, 8], [5, 70, 93, 0, 6]], 'X_OXXOO__': [[1, 7, 8], [2, 6, 39]], 'X_OXXO_O_': [[1, 6, 8], [8, 49, 75]], 'X_OX_OOX_': [[1, 4, 8], [0, 0, 10]], 'X_OX_OO_X': [[1, 4, 7], [1, 21, 1]], 'X_OX__O__': [[1, 4, 5, 7, 8], [0, 47, 9, 0, 3]], 'X_OXX_OO_': [[1, 5, 8], [7, 21, 57]], 'X_OXX_O_O': [[1, 5, 7], [1, 41, 5]], 'X_OX_XOO_': [[1, 4, 8], [2, 23, 1]], 'X_OX_XO_O': [[1, 4, 7], [2, 3, 15]], 'X_OX__OXO': [[1, 4, 5], [2, 9, 4]], 'X_OX___O_': [[1, 4, 5, 6, 8], [5, 75, 18, 7, 8]], 'X_OXX__OO': [[1, 5, 6], [1, 37, 33]], 'X_OX_X_OO': [[1, 4, 6], [10, 17, 15]], 'X_OX____O': [[1, 4, 5, 6, 7], [2, 22, 43, 75, 7]], 'X_OOX____': [[1, 5, 6, 7, 8], [86, 43, 34, 25, 19]], 'X_OOXXO__': [[1, 7, 8], [43, 27, 31]], 'X_OOXXOXO': [[1], [155]], 'X_OOXX_O_': [[1, 6, 8], [14, 20, 37]], 'X_OOXX__O': [[1, 6, 7], [22, 7, 12]], 'X_OOXO_X_': [[1, 6, 8], [31, 10, 21]], 'X_OOX_OX_': [[1, 5, 8], [9, 23, 49]], 'X_OOX__XO': [[1, 5, 6], [5, 23, 5]], 'X_O_XO___': [[1, 3, 6, 7, 8], [7, 9, 8, 18, 51]], 'X_O_XOXO_': [[1, 3, 8], [8, 19, 65]], 'X_O_XOOX_': [[1, 3, 8], [61, 0, 37]], 'X_O_X_O__': [[1, 3, 5, 7, 8], [25, 20, 50, 55, 23]], 'X_O_XXOO_': [[1, 3, 8], [3, 31, 31]], 'X_O_XXO_O': [[1, 3, 7], [7, 15, 35]], 'X_O_X_OXO': [[1, 3, 5], [39, 4, 35]], 'X_O_X__O_': [[1, 3, 5, 6, 8], [11, 33, 23, 63, 33]], 'X_O_XX_OO': [[1, 3, 6], [4, 23, 4]], 'X_O_X_XOO': [[1, 3, 5], [3, 77, 15]], 'X_O_X___O': [[1, 3, 5, 6, 7], [6, 14, 55, 23, 12]], 'X_OO_X___': [[1, 4, 6, 7, 8], [13, 22, 16, 6, 7]], 'X_OOOX_X_': [[1, 6, 8], [0, 19, 16]], 'X_OO_XOX_': [[1, 4, 8], [4, 5, 0]], 'X_OO_X_XO': [[1, 4, 6], [12, 4, 16]], 'X_OOOX__X': [[1, 6, 7], [3, 22, 3]], 'X_O_OX___': [[1, 3, 6, 7, 8], [3, 7, 34, 0, 2]], 'X_O_OXXO_': [[1, 3, 8], [25, 29, 2]], 'X_O_OXX_O': [[1, 3, 7], [16, 31, 12]], 'X_O_OX_XO': [[1, 3, 6], [0, 4, 36]], 'X_O__XO__': [[1, 3, 4, 7, 8], [8, 4, 21, 5, 5]], 'X_O__XOXO': [[1, 3, 4], [9, 4, 21]], 'X_O__X_O_': [[1, 3, 4, 6, 8], [6, 17, 12, 14, 5]], 'X_O__XXOO': [[1, 3, 4], [7, 25, 13]], 'X_O__X__O': [[1, 3, 4, 6, 7], [0, 2, 3, 6, 45]], 'X_O_O_X__': [[1, 3, 5, 7, 8], [11, 105, 15, 7, 24]], 'X_O_OOXX_': [[1, 3, 8], [3, 19, 9]], 'X_O_O_XXO': [[1, 3, 5], [4, 39, 18]], 'X_O_OOX_X': [[1, 3, 7], [4, 27, 87]], 'X_O__OX__': [[1, 3, 4, 7, 8], [13, 9, 10, 2, 146]], 'X_O___XO_': [[1, 3, 4, 5, 8], [3, 7, 74, 11, 29]], 'X_O___X_O': [[1, 3, 4, 5, 7], [3, 107, 9, 28, 8]], 'X_OO___X_': [[1, 4, 5, 6, 8], [2, 15, 9, 23, 6]], 'X_OOO__XX': [[1, 5, 6], [1, 3, 25]], 'X_OO_O_XX': [[1, 4, 6], [1, 9, 19]], 'X_O_O__X_': [[1, 3, 5, 6, 8], [0, 21, 12, 17, 23]], 'X_O_OO_XX': [[1, 3, 6], [1, 2, 11]], 'X_O__O_X_': [[1, 3, 4, 6, 8], [7, 9, 8, 8, 3]], 'X_O___OX_': [[1, 3, 4, 5, 8], [3, 1, 69, 3, 3]], 'X_O____XO': [[1, 3, 4, 5, 6], [3, 1, 11, 56, 20]], 'X_OO____X': [[1, 4, 5, 6, 7], [20, 55, 27, 46, 27]], 'X_O_O___X': [[1, 3, 5, 6, 7], [1, 2, 10, 64, 6]], 'X_O__O__X': [[1, 3, 4, 6, 7], [5, 26, 55, 48, 26]], 'X_O___O_X': [[1, 3, 4, 5, 7], [11, 3, 51, 3, 11]], 'X__O_____': [[1, 2, 4, 5, 6, 7, 8], [195, 263, 108, 149, 89, 107, 49]], 'XX_OO____': [[2, 5, 6, 7, 8], [29, 9, 10, 10, 2]], 'XX_OOXO__': [[2, 7, 8], [21, 9, 1]], 'XX_OOXOXO': [[2], [91]], 'XX_OOX_O_': [[2, 6, 8], [15, 7, 10]], 'XX_OOX__O': [[2, 6, 7], [11, 17, 11]], 'XX_OO_OX_': [[2, 5, 8], [15, 4, 1]], 'XX_OO__XO': [[2, 5, 6], [9, 19, 1]], 'XX_O_O___': [[2, 4, 6, 7, 8], [27, 25, 2, 6, 7]], 'XX_OXOO__': [[2, 7, 8], [13, 7, 33]], 'XX_OXO_O_': [[2, 6, 8], [9, 13, 27]], 'XX_OXO__O': [[2, 6, 7], [15, 4, 11]], 'XX_O_OOX_': [[2, 4, 8], [15, 11, 5]], 'XX_O_O_XO': [[2, 4, 6], [5, 33, 2]], 'XX_O__O__': [[2, 4, 5, 7, 8], [29, 13, 31, 11, 3]], 'XX_OX_OO_': [[2, 5, 8], [3, 15, 59]], 'XX_OX_O_O': [[2, 5, 7], [15, 1, 41]], 'XX_O_XOO_': [[2, 4, 8], [13, 1, 17]], 'XX_O_XO_O': [[2, 4, 7], [21, 3, 9]], 'XX_O__OXO': [[2, 4, 5], [11, 21, 35]], 'XX_O___O_': [[2, 4, 5, 6, 8], [23, 8, 13, 12, 8]], 'XX_OX__OO': [[2, 5, 6], [45, 5, 11]], 'XX_O_X_OO': [[2, 4, 6], [7, 2, 21]], 'XX_O____O': [[2, 4, 5, 6, 7], [11, 24, 12, 8, 11]], 'X_XOO____': [[1, 5, 6, 7, 8], [7, 108, 2, 14, 15]], 'X_XOOXO__': [[1, 7, 8], [41, 13, 29]], 'X_XOOX_O_': [[1, 6, 8], [71, 2, 3]], 'X_XOO_OX_': [[1, 5, 8], [13, 49, 5]], 'X_XO__O__': [[1, 4, 5, 7, 8], [33, 60, 2, 58, 36]], 'X_XOX_OO_': [[1, 5, 8], [25, 15, 65]], 'X_XO_XOO_': [[1, 4, 8], [19, 4, 11]], 'X_XO___O_': [[1, 4, 5, 6, 8], [39, 53, 17, 49, 28]], 'X__OXO___': [[1, 2, 6, 7, 8], [17, 53, 31, 77, 13]], 'X__OXOOX_': [[1, 2, 8], [31, 15, 41]], 'X__OXO_XO': [[1, 2, 6], [45, 15, 4]], 'X__OX_O__': [[1, 2, 5, 7, 8], [39, 58, 39, 42, 57]], 'X__OXXOO_': [[1, 2, 8], [7, 2, 15]], 'X__OXXO_O': [[1, 2, 7], [2, 2, 36]], 'X__OX_OXO': [[1, 2, 5], [31, 6, 23]], 'X__OX__O_': [[1, 2, 5, 6, 8], [50, 63, 2, 31, 91]], 'X__OXX_OO': [[1, 2, 6], [3, 6, 21]], 'X__OX___O': [[1, 2, 5, 6, 7], [3, 73, 39, 38, 3]], 'X__OOX___': [[1, 2, 6, 7, 8], [5, 28, 6, 35, 12]], 'X__OOXOX_': [[1, 2, 8], [3, 41, 3]], 'X__OOX_XO': [[1, 2, 6], [9, 29, 5]], 'X__O_XO__': [[1, 2, 4, 7, 8], [3, 32, 4, 0, 6]], 'X__O_XOXO': [[1, 2, 4], [15, 4, 6]], 'X__O_X_O_': [[1, 2, 4, 6, 8], [20, 25, 3, 13, 7]], 'X__O_X__O': [[1, 2, 4, 6, 7], [4, 17, 5, 20, 21]], 'X__OO__X_': [[1, 2, 5, 6, 8], [6, 10, 51, 4, 0]], 'X__O_O_X_': [[1, 2, 4, 6, 8], [5, 17, 34, 1, 3]], 'X__O__OX_': [[1, 2, 4, 5, 8], [20, 14, 18, 5, 15]], 'X__O___XO': [[1, 2, 4, 5, 6], [77, 9, 18, 13, 5]], 'X__OO___X': [[1, 2, 5, 6, 7], [4, 13, 2, 4, 11]], 'X__O_O__X': [[1, 2, 4, 6, 7], [0, 12, 31, 27, 18]], 'X___O____': [[1, 2, 3, 5, 6, 7, 8], [1, 62, 190, 28, 433, 152, 0]], 'XX__OO___': [[2, 3, 6, 7, 8], [7, 7, 2, 4, 3]], 'XX_XOOO__': [[2, 7, 8], [13, 10, 2]], 'XX_XOOOXO': [[2], [59]], 'XX_XOO_O_': [[2, 6, 8], [7, 9, 13]], 'XX_XOO__O': [[2, 6, 7], [11, 5, 8]], 'XX__OOX_O': [[2, 3, 7], [35, 43, 0]], 'XX__OOOX_': [[2, 3, 8], [15, 1, 0]], 'XX__OO_XO': [[2, 3, 6], [13, 2, 1]], 'XX__O_O__': [[2, 3, 5, 7, 8], [11, 2, 8, 3, 0]], 'XX_XO_OO_': [[2, 5, 8], [15, 1, 4]], 'XX_XO_O_O': [[2, 5, 7], [3, 1, 5]], 'XX__OXOO_': [[2, 3, 8], [5, 0, 7]], 'XX__OXO_O': [[2, 3, 7], [15, 1, 8]], 'XX__O_OXO': [[2, 3, 5], [7, 4, 1]], 'XX__O__O_': [[2, 3, 5, 6, 8], [7, 15, 3, 12, 2]], 'XX_XO__OO': [[2, 5, 6], [7, 6, 15]], 'XX__OX_OO': [[2, 3, 6], [15, 1, 7]], 'XX__O___O': [[2, 3, 5, 6, 7], [7, 5, 3, 13, 3]], 'X_X_O_O__': [[1, 3, 5, 7, 8], [113, 2, 119, 8, 44]], 'X_XXO_OO_': [[1, 5, 8], [13, 1, 3]], 'X_X_O__O_': [[1, 3, 5, 6, 8], [75, 2, 63, 21, 9]], 'X__XOO___': [[1, 2, 6, 7, 8], [10, 19, 135, 17, 20]], 'X__XOOOX_': [[1, 2, 8], [4, 5, 4]], 'X__XOO_XO': [[1, 2, 6], [11, 15, 31]], 'X__XO_O__': [[1, 2, 5, 7, 8], [6, 41, 2, 0, 1]], 'X__XOXOO_': [[1, 2, 8], [2, 1, 0]], 'X__XOXO_O': [[1, 2, 7], [3, 3, 5]], 'X__XO_OXO': [[1, 2, 5], [6, 12, 0]], 'X__XO__O_': [[1, 2, 5, 6, 8], [7, 6, 6, 99, 0]], 'X__XOX_OO': [[1, 2, 6], [2, 0, 11]], 'X__XO___O': [[1, 2, 5, 6, 7], [17, 52, 10, 11, 21]], 'X___OXO__': [[1, 2, 3, 7, 8], [6, 18, 1, 2, 22]], 'X___OXOXO': [[1, 2, 3], [1, 11, 1]], 'X___OX_O_': [[1, 2, 3, 6, 8], [20, 11, 1, 15, 4]], 'X___OX__O': [[1, 2, 3, 6, 7], [20, 38, 20, 5, 4]], 'X___OO_X_': [[1, 2, 3, 6, 8], [2, 11, 35, 1, 1]], 'X___O_OX_': [[1, 2, 3, 5, 8], [4, 9, 1, 31, 8]], 'X___O__XO': [[1, 2, 3, 5, 6], [9, 59, 17, 17, 11]], 'X____O___': [[1, 2, 3, 4, 6, 7, 8], [53, 101, 370, 83, 61, 43, 359]], 'XX___OO__': [[2, 3, 4, 7, 8], [21, 2, 9, 6, 10]], 'XX_X_OOO_': [[2, 4, 8], [9, 8, 17]], 'XX_X_OO_O': [[2, 4, 7], [9, 1, 2]], 'XX__XOOO_': [[2, 3, 8], [5, 2, 33]], 'XX__XOO_O': [[2, 3, 7], [9, 0, 19]], 'XX___OOXO': [[2, 3, 4], [17, 1, 7]], 'XX___O_O_': [[2, 3, 4, 6, 8], [7, 7, 4, 11, 19]], 'XX_X_O_OO': [[2, 4, 6], [13, 0, 7]], 'XX__XO_OO': [[2, 3, 6], [31, 1, 3]], 'XX___O__O': [[2, 3, 4, 6, 7], [15, 2, 3, 4, 2]], 'X__X_OO__': [[1, 2, 4, 7, 8], [19, 20, 21, 17, 33]], 'X__XXOOO_': [[1, 2, 8], [10, 5, 69]], 'X__XXOO_O': [[1, 2, 7], [0, 3, 1]], 'X__X_OOXO': [[1, 2, 4], [3, 26, 0]], 'X__X_O_O_': [[1, 2, 4, 6, 8], [34, 63, 27, 51, 33]], 'X__XXO_OO': [[1, 2, 6], [0, 2, 39]], 'X__X_O__O': [[1, 2, 4, 6, 7], [10, 35, 5, 93, 8]], 'X___XOO__': [[1, 2, 3, 7, 8], [9, 15, 18, 44, 15]], 'X___XOOXO': [[1, 2, 3], [69, 6, 2]], 'X___XO_O_': [[1, 2, 3, 6, 8], [25, 23, 21, 21, 37]], 'X___XO__O': [[1, 2, 3, 6, 7], [5, 78, 2, 6, 3]], 'X____OX_O': [[1, 2, 3, 4, 7], [4, 47, 171, 15, 1]], 'X____OOX_': [[1, 2, 3, 4, 8], [9, 29, 3, 6, 9]], 'X____O_XO': [[1, 2, 3, 4, 6], [18, 38, 3, 7, 4]], 'X_____O__': [[1, 2, 3, 4, 5, 7, 8], [57, 457, 11, 78, 1, 120, 243]], 'XX____OO_': [[2, 3, 4, 5, 8], [9, 5, 13, 6, 7]], 'XX____O_O': [[2, 3, 4, 5, 7], [33, 2, 4, 5, 1]], 'X__X__OO_': [[1, 2, 4, 5, 8], [6, 2, 7, 2, 17]], 'X__X__O_O': [[1, 2, 4, 5, 7], [1, 9, 5, 4, 29]], 'X___X_OO_': [[1, 2, 3, 5, 8], [1, 20, 28, 4, 63]], 'X___X_O_O': [[1, 2, 3, 5, 7], [22, 4, 16, 2, 62]], 'X____XOO_': [[1, 2, 3, 4, 8], [5, 7, 9, 2, 5]], 'X____XO_O': [[1, 2, 3, 4, 7], [6, 3, 2, 13, 8]], 'X_____OXO': [[1, 2, 3, 4, 5], [20, 44, 5, 23, 2]], 'X______O_': [[1, 2, 3, 4, 5, 6, 8], [44, 535, 35, 347, 3, 84, 15]], 'XX_____OO': [[2, 3, 4, 5, 6], [13, 3, 2, 1, 13]], 'X__X___OO': [[1, 2, 4, 5, 6], [3, 3, 4, 2, 97]], 'X___X__OO': [[1, 2, 3, 5, 6], [17, 2, 29, 8, 56]], 'X____X_OO': [[1, 2, 3, 4, 6], [1, 10, 2, 5, 7]], 'X_______O': [[1, 2, 3, 4, 5, 6, 7], [31, 43, 256, 0, 86, 272, 211]], 'OX_______': [[2, 3, 4, 5, 6, 7, 8], [5, 10, 375, 14, 100, 30, 139]], 'OXOX_____': [[4, 5, 6, 7, 8], [15, 3, 3, 7, 11]], 'OXOXXO___': [[6, 7, 8], [2, 59, 15]], 'OXOXX_O__': [[5, 7, 8], [17, 25, 47]], 'OXOXX__O_': [[5, 6, 8], [41, 14, 14]], 'OXOXX___O': [[5, 6, 7], [21, 0, 49]], 'OXOXOX___': [[6, 7, 8], [3, 2, 1]], 'OXOX_XO__': [[4, 7, 8], [7, 5, 1]], 'OXOX_XOXO': [[4], [13]], 'OXOX_X_O_': [[4, 6, 8], [5, 3, 3]], 'OXOX_X__O': [[4, 6, 7], [5, 2, 6]], 'OXOXO__X_': [[5, 6, 8], [3, 7, 5]], 'OXOX_O_X_': [[4, 6, 8], [3, 3, 11]], 'OXOX___XO': [[4, 5, 6], [3, 4, 1]], 'OX_XO____': [[2, 5, 6, 7, 8], [1, 1, 5, 3, 5]], 'OX_XOXO__': [[2, 7, 8], [9, 2, 3]], 'OX_XOX_O_': [[2, 6, 8], [2, 2, 11]], 'OX_XOO_X_': [[2, 6, 8], [6, 2, 16]], 'OX_X_O___': [[2, 4, 6, 7, 8], [11, 9, 5, 5, 7]], 'OX_XXOO__': [[2, 7, 8], [16, 49, 4]], 'OX_XXO_O_': [[2, 6, 8], [16, 13, 3]], 'OX_XXO__O': [[2, 6, 7], [33, 4, 25]], 'OX_X_O_XO': [[2, 4, 6], [5, 3, 2]], 'OX_X__O__': [[2, 4, 5, 7, 8], [4, 13, 14, 3, 15]], 'OX_XX_OO_': [[2, 5, 8], [1, 59, 13]], 'OX_XX_O_O': [[2, 5, 7], [4, 39, 31]], 'OX_X_XOO_': [[2, 4, 8], [2, 17, 3]], 'OX_X_XO_O': [[2, 4, 7], [2, 17, 3]], 'OX_X___O_': [[2, 4, 5, 6, 8], [6, 3, 10, 7, 17]], 'OX_XX__OO': [[2, 5, 6], [1, 9, 35]], 'OX_X_X_OO': [[2, 4, 6], [0, 19, 7]], 'OX_X____O': [[2, 4, 5, 6, 7], [2, 8, 7, 5, 1]], 'OXO_X____': [[3, 5, 6, 7, 8], [34, 109, 10, 17, 22]], 'OX_OX____': [[2, 5, 6, 7, 8], [71, 8, 39, 51, 28]], 'OX_OXX_O_': [[2, 6, 8], [9, 9, 4]], 'OX_OXX__O': [[2, 6, 7], [8, 11, 15]], 'OX__XO___': [[2, 3, 6, 7, 8], [56, 16, 40, 49, 16]], 'OX__X_O__': [[2, 3, 5, 7, 8], [4, 68, 13, 75, 1]], 'OX__XXOO_': [[2, 3, 8], [1, 29, 1]], 'OX__XXO_O': [[2, 3, 7], [2, 21, 17]], 'OX__X__O_': [[2, 3, 5, 6, 8], [18, 7, 17, 61, 7]], 'OX__XX_OO': [[2, 3, 6], [3, 23, 3]], 'OX__X___O': [[2, 3, 5, 6, 7], [7, 51, 21, 41, 81]], 'OX_O_X___': [[2, 4, 6, 7, 8], [1, 3, 20, 3, 7]], 'OX_OOX_X_': [[2, 6, 8], [2, 9, 5]], 'OX__OX___': [[2, 3, 6, 7, 8], [1, 1, 5, 2, 26]], 'OX__OXOX_': [[2, 3, 8], [1, 1, 1]], 'OX___XO__': [[2, 3, 4, 7, 8], [2, 2, 12, 3, 4]], 'OX___X_O_': [[2, 3, 4, 6, 8], [7, 13, 4, 3, 6]], 'OX___X__O': [[2, 3, 4, 6, 7], [0, 3, 13, 3, 0]], 'OXO____X_': [[3, 4, 5, 6, 8], [5, 17, 6, 4, 9]], 'OX_O___X_': [[2, 4, 5, 6, 8], [3, 3, 7, 5, 2]], 'OX__O__X_': [[2, 3, 5, 6, 8], [0, 3, 2, 1, 1]], 'OX___O_X_': [[2, 3, 4, 6, 8], [3, 5, 5, 14, 9]], 'OX____OX_': [[2, 3, 4, 5, 8], [6, 4, 19, 2, 1]], 'OX_____XO': [[2, 3, 4, 5, 6], [5, 5, 5, 3, 2]], '_XO______': [[0, 3, 4, 5, 6, 7, 8], [17, 18, 407, 41, 41, 36, 54]], '_XOXO____': [[0, 5, 6, 7, 8], [1, 10, 17, 1, 6]], '_XOXOO_X_': [[0, 6, 8], [2, 6, 3]], '_XOX_O___': [[0, 4, 6, 7, 8], [6, 7, 4, 8, 4]], '_XOXXO_O_': [[0, 6, 8], [1, 9, 38]], '_XOX___O_': [[0, 4, 5, 6, 8], [5, 15, 2, 34, 10]], '_XOXX__OO': [[0, 5, 6], [0, 31, 0]], '_XOX____O': [[0, 4, 5, 6, 7], [7, 4, 3, 3, 6]], '_XOOX____': [[0, 5, 6, 7, 8], [37, 8, 44, 53, 82]], '_XO_XO___': [[0, 3, 6, 7, 8], [20, 9, 5, 101, 35]], '_XO_X_O__': [[0, 3, 5, 7, 8], [73, 10, 42, 53, 19]], '_XO_X__O_': [[0, 3, 5, 6, 8], [5, 31, 67, 17, 9]], '_XO_X___O': [[0, 3, 5, 6, 7], [0, 0, 78, 18, 83]], '_XOO___X_': [[0, 4, 5, 6, 8], [7, 13, 6, 8, 10]], '_XO_O__X_': [[0, 3, 5, 6, 8], [4, 0, 7, 4, 7]], '_XO__O_X_': [[0, 3, 4, 6, 8], [1, 8, 21, 5, 7]], '_XO___OX_': [[0, 3, 4, 5, 8], [2, 1, 5, 6, 4]], '_X_O_____': [[0, 2, 4, 5, 6, 7, 8], [61, 136, 387, 12, 37, 8, 19]], '_X_OXO___': [[0, 2, 6, 7, 8], [15, 21, 21, 119, 35]], '_X_OX_O__': [[0, 2, 5, 7, 8], [72, 10, 11, 35, 11]], '_X_OXXOO_': [[0, 2, 8], [3, 0, 4]], '_X_OX__O_': [[0, 2, 5, 6, 8], [20, 28, 9, 33, 24]], '_X_OX___O': [[0, 2, 5, 6, 7], [22, 48, 57, 7, 71]], '_X_OOX___': [[0, 2, 6, 7, 8], [14, 18, 3, 3, 11]], '_X_O_XO__': [[0, 2, 4, 7, 8], [9, 4, 2, 4, 8]], '_X_O_X_O_': [[0, 2, 4, 6, 8], [13, 9, 5, 24, 24]], '_X_OO__X_': [[0, 2, 5, 6, 8], [2, 1, 6, 3, 1]], '_X_O_O_X_': [[0, 2, 4, 6, 8], [5, 3, 5, 2, 3]], '_X__O____': [[0, 2, 3, 5, 6, 7, 8], [18, 114, 39, 25, 182, 1, 47]], '_X_XOO___': [[0, 2, 6, 7, 8], [2, 9, 12, 11, 12]], '_X_XO___O': [[0, 2, 5, 6, 7], [11, 4, 0, 0, 1]], '_X___O___': [[0, 2, 3, 4, 6, 7, 8], [16, 138, 66, 236, 54, 27, 103]], '_X_X_O__O': [[0, 2, 4, 6, 7], [3, 6, 5, 6, 6]], '_X__XOO__': [[0, 2, 3, 7, 8], [39, 40, 5, 43, 7]], '_X__XO_O_': [[0, 2, 3, 6, 8], [11, 17, 11, 13, 16]], '_X__XO__O': [[0, 2, 3, 6, 7], [5, 13, 7, 31, 103]], '_X____O__': [[0, 2, 3, 4, 5, 7, 8], [52, 75, 45, 260, 5, 51, 123]], '_X__X_OO_': [[0, 2, 3, 5, 8], [15, 2, 6, 8, 23]], '_X__X_O_O': [[0, 2, 3, 5, 7], [20, 14, 11, 2, 107]], '_X_____O_': [[0, 2, 3, 4, 5, 6, 8], [31, 314, 119, 7, 16, 46, 141]], '_X__X__OO': [[0, 2, 3, 5, 6], [12, 36, 4, 14, 6]], '_X______O': [[0, 2, 3, 4, 5, 6, 7], [18, 246, 11, 268, 48, 13, 1]], 'O___X____': [[1, 2, 3, 5, 6, 7, 8], [191, 307, 260, 36, 73, 158, 255]], '_O__X____': [[0, 2, 3, 5, 6, 7, 8], [138, 668, 179, 177, 131, 33, 73]]}