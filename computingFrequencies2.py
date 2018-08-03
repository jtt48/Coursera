import sys
import re
import json
import glob
import linecache
# messed up, this has nothing to do with compFreq, its actually frequent words with mismatches
def computingFrequencies(text, k):
    k = int(k)
    print("K: ",k)
    allKs = {}
    kmers = allKmers(k)
    for i in range(len(kmers)):
        allKs[kmers[i]] = 0
    print(allKs)

    

def allKmers(k):
    if k == 1:
        return ["g","c","a","t"]
    re = reBuild("g",allKmers(k - 1))
    re.extend(reBuild("c",allKmers(k-1)))
    re.extend(reBuild("a",allKmers(k-1)))
    re.extend(reBuild("t",allKmers(k-1)))
    return re

def reBuild(letter,array):
    for i in range(len(array)):
        array[i] = letter + array[i]
    return array

with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        param = input.read().splitlines()
        res = computingFrequencies(param[0],param[1])
        #print(allKmers(3))
        #output.write(res)
