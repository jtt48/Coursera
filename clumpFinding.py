import sys
import re
import json
import glob
import linecache

# store all combinations of X letters in dict
# go through dict if more than Y -1  entries in that key
# check if the entries are less than Z entires appart (each entry should be position found)
# if Y of them are in range Z add Key to output.


def findClumps(data,length2,windowSize2,hitsNmb2):

    length = int(length2)
    windowSize = int(windowSize2)
    hitsNmb = int(hitsNmb2)
    
    theDict = {}
    result = "" 
    result2 = 0
    
    for i in range(len(data)):
        if i == len(data) - (length):
            print((data[i:(i + length)]))
            #print(theDict)
            #return
            break

        theDict.setdefault(data[i:(i + length)], []).append(i)

    #print(theDict)
    #print("Dictionary Made")

    keys = list(theDict.keys())

    for key in keys:
        #print(key)
        if len(theDict[key]) >= hitsNmb:
            arr = theDict[key]

            for x in range(len(arr)):
                if x > len(arr) - hitsNmb:
                    break
                #print("x: " + str(arr[x]))
                #print("Window Size: " + str(windowSize))
                cap = arr[x] + windowSize
                #print("Cap: " + str(cap))
                count = 0
                for y in range(hitsNmb):
                    #print("Check for " + key + ":" + str(x) +" = " +str(arr[y + x]))
                    if arr[y + x] + (length) <= cap:
                        count = count + 1
                        #print(count)
                    else:
                        break
                if count >= hitsNmb:
               #     print("KEY: " + key)
                    #result = result + " " + key
                    result2 = result2 + 1
                    break

                    
    return str(result2)





with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        inp = input.read().splitlines()    
        output.write(findClumps(inp[0],inp[1],inp[2],inp[3]))
