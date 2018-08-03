import sys
import re
import json
import glob
import linecache

def computingFrequencies(text, k):
    
    frequencyArray = list()
    for i in range(k - 1)):
        frequencyArray.append(0)

    for i in range(len(text) - k):
        pattern = patternToNumber(text[i],k)

with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        
        param = input.read().splitlines()
        res = patternMatch(param[0],param[1])
        print(res)
        output.write(res)


