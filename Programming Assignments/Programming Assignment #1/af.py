import sys
import numpy as np
import csv
from fs import *
from hs import *    #h(s) function
from a11 import bfs
from a12 import dfs
from a13 import iddfs
from a14 import astart

initState = []
goalState = []

#validate command argument, should include file name qand search type
if(len(sys.argv)!=5):
    print("ERR: Please Include Data File or Search Type ", len(sys.argv))
    sys.exit(0)

#read and pare initinal
initState = getInitState(sys.argv[1])
goalState = getInitState(sys.argv[2])

print("Inital State:")
print(initState)
print("Goal State")
print(goalState)

if str(sys.argv[3]) == "bfs":
        bfs(initState, sys.argv[4])
elif str(sys.argv[3]) == "dfs":
        dfs(initState, sys.argv[4])
elif str(sys.argv[3]) == "iddfs":
        iddfs(initState, sys.argv[4])
elif str(sys.argv[3]) == "astart":
        astart(initState, sys.argv[4])
else:
    print("Err: No Match Search Method")
