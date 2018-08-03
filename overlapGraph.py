import sys
import re
import json
import glob
import linecache

def overlapGraph(text):
    
    #compare results and next, if they dont match we slice offf
    # a letter and compare the slices, doing this till we have
    # a match we can merge on.

    print("overlapGraph")
    node = ""
    results = ""
    for i in range(len(text)):
        node = text[i].strip()
        #print("node: " + node)
        possibleRes = node + " -> "
        tog = 0
        for j in range(len(text)):
            next = text[j].strip()
            if node !=  next:
                #print("next: " + next)
                prefix = node[1:]
                suffix = next[0:len(next)- 1]
                #print("prefix: ", prefix, " Suffix:", suffix)
                if prefix == suffix:
                    if tog > 0:
                        possibleRes = possibleRes + "," +  next
                    else:
                        possibleRes = possibleRes +  next
                    tog = tog + 1
        #print("tog", tog)
        if tog != 0:
            results = results + possibleRes + "\n"
            tog = 0
        #print("current results: ", results)
    return str(results)

with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        
        param = input.read().splitlines()
        
        text = param[0:]
        #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
        output.write(overlapGraph(text))
