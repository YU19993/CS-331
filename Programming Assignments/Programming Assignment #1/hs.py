import sys
import numpy as np
import csv
from fs import *

def h(initState):
        expend = 0
        states = []
        states.append([])
        states[0].append(initState)
        used = []
        while(len(states) != 0 and checkWin(states[0][len(states[0])-1]) == False):
                currentState = states.pop(0)
                current = len(currentState)-1
                if(currentState[current][2] == 1):
                        #print("In left: ", currentState[current], " \n")
                        #send one wolve
                        if(currentState[current][1] >= 1):
                            #    print("11\n")
                                t = cl(currentState[current])
                                t[1] = t[1] - 1
                                t[4] = t[4] + 1
                                t[2] = 0
                                t[5] = 1
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)
                        #send two wolves
                        if(currentState[current][1] >= 2):
                            #    print("12\n")
                                t = cl(currentState[current])
                                t[1] = t[1] - 2
                                t[4] = t[4] + 2
                                t[2] = 0
                                t[5] = 1
                            #    print(t)
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)
                        #send one chicken
                        if(currentState[current][0] >= 1):
                            #    print("13\n")
                                t = cl(currentState[current])
                                t[0] = t[0] - 1
                                t[3] = t[3] + 1
                                t[2] = 0
                                t[5] = 1
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)
                        #send two chickens
                        if(currentState[current][0] >= 2):
                            #    print("14\n")
                                t = cl(currentState[current])
                                t[0] = t[0] - 2
                                t[3] = t[3] + 2
                                t[2] = 0
                                t[5] = 1
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)
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
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)

                else:
                        #send one wolve
                        if(currentState[current][4] >= 1):
                            #    print("21\n")
                                t = cl(currentState[current])
                                t[4] = t[4] - 1
                                t[1] = t[1] + 1
                                t[5] = 0
                                t[2] = 1
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)
                        #send two wolves
                        if(currentState[current][4] >= 2):
                            #    print("22\n")
                                t = cl(currentState[current])
                                t[4] = t[4] - 2
                                t[1] = t[1] + 2
                                t[5] = 0
                                t[2] = 1
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)
                        #send one chicken
                        if(currentState[current][3] >= 1):
                                #print("23\n")
                                t = cl(currentState[current])
                                t[0] = t[0] + 1
                                t[3] = t[3] - 1
                                t[5] = 0
                                t[2] = 1
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)
                        #send two chickens
                        if(currentState[current][3] >= 2):
                            #    print("24\n")
                                t = cl(currentState[current])
                                t[0] = t[0] + 2
                                t[3] = t[3] - 2
                                t[5] = 0
                                t[2] = 1
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)
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
                                if(checkIn(t, used) and checkIn(t, currentState) and checkState(t)):
                                        used.append(t)
                                        st = cll(currentState)
                                        st.append(t)
                                        states.append(st)
                                        expend = expend + 1
                                        #print(states)
        if(len(states) > 0):
                return int(len(states[0])-1)
        else:
                return int(-1)
