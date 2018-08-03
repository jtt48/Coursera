import sys
import re
import json
import glob
import linecache

def skew(genome):
    
    print("starting skew")
    maxCount = 0
    count = 0
    rstring = ""
    print("Len ",len(genome))
    for i in range(len(genome)):
#        print(genome[i])
        if i == len(genome) - 1:
            return rstring
        #print(genome[i])
        if genome[i] == "C":
            count = count -1
            if count == maxCount:
                rstring = rstring + " " + str(i + 1)
        if genome[i] == "G":
            count =  count +1
        print("Well? ",count < maxCount)
        if count > maxCount:
            print("new MAX count")
            maxCount = count
            rstring = str(i + 1)
        print("Count: ",count)
        print("MC", maxCount)
        print()

    return rstring




with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        
        param = input.read().splitlines()
        
        res = skew(param[0])
        
        output.write(res)


