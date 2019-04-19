import sys
import numpy as np
import csv
from fs import *
from hs import *    #h(s) function

def astart(initState, out):
        expend = 0
        states = []
        states.append([])
        states[0].append(initState)
        while(len(states) != 0 and checkWin(states[0][len(states[0])-1]) == False):
                currentState = states.pop(0)
                current = len(currentState)-1
                bestNode = []
                bestValue = -1
                hs = -1
                if(currentState[current][2] == 1):
                        print("In left: ", currentState[current], " \n")
                        #send one wolve
                        if(currentState[current][1] >= 1):
                            #    print("11\n")
                                t = cl(currentState[current])
                                t[1] = t[1] - 1
                                t[4] = t[4] + 1
                                t[2] = 0
                                t[5] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs
                        #send two wolves
                        if(currentState[current][1] >= 2):
                            #    print("12\n")
                                t = cl(currentState[current])
                                t[1] = t[1] - 2
                                t[4] = t[4] + 2
                                t[2] = 0
                                t[5] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs

                        #send one chicken
                        if(currentState[current][0] >= 1):
                            #    print("13\n")
                                t = cl(currentState[current])
                                t[0] = t[0] - 1
                                t[3] = t[3] + 1
                                t[2] = 0
                                t[5] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs
                        #send two chickens
                        if(currentState[current][0] >= 2):
                            #    print("14\n")
                                t = cl(currentState[current])
                                t[0] = t[0] - 2
                                t[3] = t[3] + 2
                                t[2] = 0
                                t[5] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs
                        #send one chicken and one wolve
                        if((currentState[current][1] >= 1) and (currentState[current][0] >= 1)):
                            #    print("15\n")
                                t = cl(currentState[current])
                                t[1] = t[1] - 1
                                t[4] = t[4] + 1
                                t[0] = t[0] - 1
                                t[3] = t[3] + 1
                                t[2] = 0
                                t[5] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs

                else:
                        print("In Right: ", currentState[current], " \n")
                        #send one wolve
                        if(currentState[current][4] >= 1):
                            #    print("21\n")
                                t = cl(currentState[current])
                                t[4] = t[4] - 1
                                t[1] = t[1] + 1
                                t[5] = 0
                                t[2] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs
                        #send two wolves
                        if(currentState[current][4] >= 2):
                            #    print("22\n")
                                t = cl(currentState[current])
                                t[4] = t[4] - 2
                                t[1] = t[1] + 2
                                t[5] = 0
                                t[2] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs
                        #send one chicken
                        if(currentState[current][3] >= 1):
                                #print("23\n")
                                t = cl(currentState[current])
                                t[0] = t[0] + 1
                                t[3] = t[3] - 1
                                t[5] = 0
                                t[2] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs
                        #send two chickens
                        if(currentState[current][3] >= 2):
                            #    print("24\n")
                                t = cl(currentState[current])
                                t[0] = t[0] + 2
                                t[3] = t[3] - 2
                                t[5] = 0
                                t[2] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs
                        #send one chicken and one wolve
                        if((currentState[current][3] >= 1) and (currentState[current][4] >= 1)):
                            #    print("25\n")
                                t = cl(currentState[current])
                                t[1] = t[1] + 1
                                t[4] = t[4] - 1
                                t[0] = t[0] + 1
                                t[3] = t[3] - 1
                                t[5] = 0
                                t[2] = 1
                                hs = h(t)
                                if(checkIn(t, currentState) and checkState(t) and hs != -1):
                                        if(bestValue == -1):
                                                bestNode = cl(t)
                                                bestValue = hs
                                        elif(hs < bestValue):
                                                bestNode = cl(t)
                                                bestValue = hs
                if(bestValue != -1):
                        st = cll(currentState)
                        st.append(bestNode)
                        states.append(st)
                        expend = expend + 1
        for x in states[0]:
            print(x)
        print("Expend: ", expend)
        file = open(out, "w")
        for x in states[0]:
            file.write(str(x) + "\n")
        file.close()
