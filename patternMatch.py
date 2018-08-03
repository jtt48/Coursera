import sys
import re
import json
import glob
import linecache

def patternMatch(pattern, genome):
    
    rstring = ""
    psize = len(pattern)


    for i in range(len(genome)):
        if i == len(genome) - psize:
            return rstring
        if genome[i:(i + psize)] == pattern:
            rstring = rstring + " " + str(i) + " "

    return rstring



with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        
        param = input.read().splitlines()
        res = patternMatch(param[0],param[1])
        print(res)
        output.write(res)


