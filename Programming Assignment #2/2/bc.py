import sys

#valide command argument
def validSys(sa):
        if len(sa) != 3:
                print("ERR: Argumnet Len is ", len(sa))
                exit(1)

        if sa[1] != "human" and sa[1] != "minmax":
                print("ERR: Player 1 Has Incorrect Type")
                exit(0)

        if sa[2] != "human" and sa[2] != "minmax":
                print("ERR: Player 2 Has Incorrect Type")
                exit(0)

#print the board
def printBoard(bd):
        for i in range(len(bd)):
                for ii in range(len(bd[0])):
                            print("----", end='')
                print("-")
                for ii in range(len(bd[0])):
                            print("|", end='')
                            if   bd[i][ii] > 0:
                                    print(" X ", end='')
                            elif bd[i][ii] < 0:
                                    print(" O ", end='')
                            else:
                                    print(" ~ ", end='')
                print("|")
        for i in range(len(bd[0])):
                print("----", end='')
        print("-", flush=True)

#check if there is utility and check the quality of the utility
#the quality is defined by the number of piece each user has

def utility(bd):
        x = 0
        o = 0
        #print("In utility: ", len(bd), "  ", len(bd[3]))
        for i in range(4):
                for ii in range(4):
                        if bd[i][ii] == 1:
                                x = x + 1
                        elif bd[i][ii] == -1:
                                o = o - 1
        return int(x + o)

def scores(bd):
        x = 0
        o = 0
        #print("In utility: ", len(bd), "  ", len(bd[3]))
        for i in range(4):
                for ii in range(4):
                        if bd[i][ii] == 1:
                                x = x + 1
                        elif bd[i][ii] == -1:
                                o = o - 1
        print("X: ", x)
        print("O: ", abs(o))

def complete(bd):
        x = 0
        o = 0
        z = 0
        #print("In utility: ", len(bd), "  ", len(bd[3]))
        for i in range(4):
                for ii in range(4):
                        if bd[i][ii] == 0:
                                z = z + 1
        return z

def checkwin(bd):
        m1 = successor(bd, 1)
        m2 = successor(bd, -1)
        if complete(bd) == 0:
                if utility(bd) > 0:
                        print("Player X is winning")
                else:
                        print("Player O is winning")
                return True
        elif len(m1[0]) == 0 and len(m2[0]) == 0:
                print("The game reachs a tie.")
                return True
        else:
                return False



#initial the printBoard
def initBoard():
        board = []
        for x in range(4):
                board.append([])
                for xx in range(4):
                        board[x].append(0)

        board[1][1] =  1
        board[2][2] =  1
        board[1][2] = -1
        board[2][1] = -1
        return board

def copyBoard(bd):
        board = []
        for x in range(4):
                board.append([])
                for xx in range(4):
                        board[x].append(bd[x][xx])
        return board

#find all possible for next move given the play type: first or second
def successor(bd, pl):
        #print("in successor: ", pl)
        #printBoard(bd)
        s = []
        d = []
        find = False
        if pl == 1:
                po = -1
        else:
                po =  1
        for i in range(len(bd)):
                for ii in range(len(bd[0])):
                        #un-used
                        if bd[i][ii] == 0:
                                #up direction
                                if i-1 <= 3 and i-1 >= 0:
                                        if bd[i-1][ii] == po:
                                                t = i - 2
                                                find = False
                                                while t >= 0:
                                                        if bd[t][ii] == pl:
                                                                find = True
                                                        t = t-1
                                                if find:
                                                        tt = []
                                                        tt.append(i)
                                                        tt.append(ii)
                                                        s.append(tt)
                                                        d.append(0)
                                #down dir
                                if i+1 <= 3 and i+1 >= 0:
                                        if bd[i+1][ii] == po:
                                                t = i + 2
                                                find = False
                                                while t <= 3:
                                                        if bd[t][ii] == pl:
                                                                find = True
                                                        t = t+1
                                                if find:
                                                        tt = []
                                                        tt.append(i)
                                                        tt.append(ii)
                                                        s.append(tt)
                                                        d.append(1)
                                #left dir
                                if ii-1 <= 3 and ii-1 >= 0:
                                        if bd[i][ii-1] == po:
                                                t = ii - 2
                                                find = False
                                                while t >= 0:
                                                        if bd[i][t] == pl:
                                                                find = True
                                                        t = t-1
                                                if find:
                                                        tt = []
                                                        tt.append(i)
                                                        tt.append(ii)
                                                        s.append(tt)
                                                        d.append(2)
                                #right dir
                                if ii+1 <= 3 and ii+1 >= 0:
                                        if bd[i][ii+1] == po:
                                                t = ii + 2
                                                find = False
                                                while t <= 3:
                                                        if bd[i][t] == pl:
                                                                find = True
                                                        t = t+1
                                                if find:
                                                        tt = []
                                                        tt.append(i)
                                                        tt.append(ii)
                                                        s.append(tt)
                                                        d.append(3)
        r = []
        r.append(s)
        r.append(d)
        #print("successor: ", r)
        return r

#flip the pieces
def flipPieces(move, bd, row, col, pl, d):
        #print("in flip", row, "  ", col, "  ", pl, "  ", d)
        #print(move)
        #printBoard(bd)
        bd[row][col] = int(pl)
        if d == 0:
                t = 1
                #print("up")
                while bd[row-t][col] != pl:
                        bd[row-t][col] = pl
                        t=t+1
        elif d == 1:
                t = 1
                #print("down")
                while bd[row+t][col] != pl:
                        bd[row+t][col] = pl
                        t=t+1
        elif d == 2:
                t = 1
                #print("left")
                while bd[row][col-t] != pl:
                        bd[row][col-t] = pl
                        t=t+1
        elif d == 3:
                t = 1
                #print("right")
                while bd[row][col+t] != pl:
                        #print(col+t)
                        bd[row][col+t] = pl
                        t=t+1
        #printBoard(bd)
        return bd

def humPlay(bd, pl):
        if pl == 1:
                po = -1
                print("Player X is in Position")
        else:
                po =  1
                print("Player O is in Position")
        move = successor(bd, pl)
        scores(bd)
        if len(move[0]) == 0:
                print("Player ", end ='')
                if pl == 1:
                     print("X: You have no possible move.")
                else:
                     print("O: You have no possible move.")
                return bd
        else:
                printBoard(bd)
                d = -1
                a = -1
                print("Please enter your move, ", end='')
                if pl == 1:
                        print("X")
                else:
                        print("O")
                row = int(input("Row:    "))
                col = int(input("Column: "))
                find = False
                for x in range(len(move[0])):
                        if row == move[0][x][0] and col == move[0][x][1]:
                                find = True
                                d = move[1][x]
                                a = x
                if not find:
                        print("In valid move")

                while not find:
                        print("Please enter your move, ", end='')
                        if pl == 1:
                                print("X")
                        else:
                                print("O")
                        row = int(input("Row:    "))
                        col = int(input("Column: "))
                        find = False
                        for x in range(len(move[0])):
                                if row == move[0][x][0] and col == move[0][x][1]:
                                        find = True
                                        d = move[1][x]
                                        a = x
                        if not find:
                                print("In valid move")


        #printBoard(bd)
        return flipPieces(move, bd, row, col, pl, d)

def minmax(bd, pl):
        move = successor(copyBoard(bd), pl)
        score = []
        if pl == 1:
                po = -1
        else:
                po =  1
        #print(move[0])
        if len(move[0]) == 0:   #no possible move
                #print("successor", len(move[0]))
                return utility(bd)
        else:
                for x in range(len(move[0])):
                        t = copyBoard(bd)
                        tt = flipPieces(move, t, move[0][x][0], move[0][x][1], pl, move[1][x])
                        score.append(minmax(tt, po))
                if pl == 1:
                        #print(max(score))
                        return max(score)
                else:
                        #print(min(score))
                        return min(score)

def minmaxPlay(bd, pl):
        move = successor(bd, pl)
        score = []
        a = -1
        if pl == 1:
                po = -1
                print("Player X is in position.")
        else:
                po =  1
                print("Player O is in Position")
        ut = 0
        scores(bd)
        printBoard(bd)
        if len(move[0]) == 0:
                    print("AL player current has no move.")
                    return bd
        for x in range(len(move[0])):
                t = copyBoard(bd)
                tt = flipPieces(move, t, move[0][x][0], move[0][x][1], pl, move[1][x])
                score.append(minmax(tt, po))
        if pl == 1:
                ut = max(score)
        else:
                ut = min(score)
        for x in range(len(score)):
                if score[x] == ut:
                        a = x
        print("Minmax is playing")
        return flipPieces(move, bd, move[0][a][0], move[0][a][1], pl, move[1][a])
