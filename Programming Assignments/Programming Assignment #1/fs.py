import sys
import numpy as np
import csv

def checkWin(a):
        if(a[3] == 0 and a[4] == 0 and a[5] == 0):
                return True
        return False

def getInitState(a):
        initState = []

        #read and pare initinal
        with open(a) as file:
                data = csv.reader(file)
                for x in data:
                        for xx in x:
                                initState.append(int(xx))
        return initState

def checkState(a):
        if((a[1] - a[0]) <= 0 and (a[4] - a[3]) <= 0):
                #print("In checkState: True")
                return True
        elif((a[1] - a[0]) > 0 and a[0] == 0 and (a[4] - a[3]) <= 0):
                #print("In checkState: True")
                return True
        elif((a[1] - a[0]) < 0 and a[3] == 0 and (a[4] - a[3]) > 0):
                #print("In checkState: True")
                return True
        #print("In checkState: False")
        return False

def checkEq(a, b):
        if(a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] == b[3] and a[4] == b[4] and a[5] == b[5]):
                return True
        return False

def checkIn(a, b):
        for x in b:
                if(checkEq(a, x)):
                        #print("In checkIn: False")
                        return False
        #print("In checkIn: True")
        return True

def cl(a):
    t = []
    for x in a:
        t.append(x)
    return t

def cll(a):
    t = []
    for x in a:
        tt = []
        for xx in x:
            tt.append(xx)
        t.append(tt)
    return t
