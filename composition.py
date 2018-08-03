import sys
import re
import json
import glob
import linecache
from profileMostProbableKmer import profileMostProbableKmer

def composition (text, k):
    
    print("starting compostion")
    results = []
    k = int(k)
    for i in range(len(text) - k + 1):
        window = text[i:i+k]
        results.append(window)
    alphabetize(results)
    resultsString = ""
    for x in results:
        resultsString = resultsString + str(x) + "\n"
    return str(resultsString)

# aplhabetize an array
def alphabetize(arr):
    arr.sort()
    return arr


with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        
        param = input.read().splitlines()
        
        k = param[0]
        text = param[1]
        #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
        output.write(composition(text,k))
