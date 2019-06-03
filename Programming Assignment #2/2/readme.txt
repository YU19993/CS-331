CS 331 Assignment #2: Simplified Othello
Name: Mingyu Zhang
Data: May 3, 2019

Run in python 3.7 and by the command:

      python Othello.py player1 player_2


Test in the command:

      python Othello.py human minmax

Description:
This assignment implements the Simplified Othello with a 4X4 board, and the implementation includes:
    utility function based the advantage on winning
    successor function finds all possible movement in up, down, left and right direction
    minmax function to find best successor
    bookkeeping functions to track wining state and other functionality to help the implementation

The test is based on the assumption that human play first and minmax play second, and there is a tie in the test case.
