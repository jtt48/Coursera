import sys
import re
import json
import glob
import linecache
import random
import copy
from eulerianPairPath import eulerianPairPath
from debruijnPairGraph import debruijnPairGraph

def reconstructionFromReadPair(text,k,d):
    graph = debruijnPairGraph(text)
    thing = eulerianPairPath(graph)
    print(thing)
    return ""
   
if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
            k = param[0]
            d = param[1]
            text = param[2:]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(reconstructionFromReadPair(text,k,d))
