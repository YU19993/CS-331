import sys
from bc import *

validSys(sys.argv)

#initial the board
board = initBoard()

player_1 = str(sys.argv[1])
player_2 = str(sys.argv[2])

win = False

while not win:
        m = successor(board, 1)
        if len(m[0]) >0:
                if player_1 == "human":
                        board = humPlay(board, 1)
                else:
                        board = minmaxPlay(board, 1)
                printBoard(board)
        m = successor(board, -1)
        if len(m[0]) >0:
                if player_2 == "human":
                        board = humPlay(board, -1)
                else:
                        board = minmaxPlay(board, -1)
                printBoard(board)
        win = checkwin(board)
