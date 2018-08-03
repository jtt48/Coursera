import sys
import re
import json
import glob
import linecache

with open(sys.argv[1], "r+") as input:
    with open("CountOutput.txt", "w+") as output:
        
        f = input.read().splitlines()
        count = 0
        #value = input.read().split('/n')[0]
        
        #value = linecache.getline(sys.argv[1],3)

        #inp = linecache.getline(sys.argv[1],2) 
        
        value = int(f[1])

        inp = f[0]

        thisDict = {}

        for i in range(len(inp) - 1):
            #print((len(value)))
                
                key = inp[i:(i + value)]
                thisDict.setdefault(key,0)
                thisDict[key] = thisDict[key] + 1
        
        
        keys = list(thisDict.keys())
        rstring = ""
        count = 0
        for k in keys:
            if thisDict[k] > count:
                count = thisDict[k]
        for k in keys:
            if thisDict[k] == count:
                rstring = rstring + " " + k
        print(thisDict)
        output.write(rstring)
