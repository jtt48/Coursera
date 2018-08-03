import sys
import re
import json
import glob
import linecache

def debruijnGraph(text,k):
    #text = stringToKmers(dna,k)
    print("k: " , k)
    k = int(k) - 1
    
    #grab all kmers and store in a dict the shared k-1mers between themselves and store
    #the next k-1mer attached to it and append it to the value

    #stil dont really get any of this, but it gets the right result.
    
    dict = {}
    print("started debruijnGraph")
    node = ""
    results = ""
    lastNode = ""
    for i in range(len(text) - k + 1):
        node = text[i:i+k]
        print("node: ", node)
        if node not in dict:
            dict[node] = []
        if lastNode != "":
            dict[lastNode].append(node)
        lastNode = node

        keys=[]
    for key2 in dict:
        keys.append(key2)
    keys.sort()

    for key in keys:
        entry = key + " -> "
        tog = 0
        sortedDict = dict[key]
        sortedDict.sort()
        for res in sortedDict:
            if tog == 0:
                entry = entry + res
                tog = tog + 1
            else:
                entry = entry + "," + res
        entry = entry + "\n"
        if tog > 0:
            results = results + entry
    return results

if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
            k = param[0]
            text = param[1]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(debruijnGraph(text,k))
