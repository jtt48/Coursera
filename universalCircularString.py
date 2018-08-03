import sys
import re
import json
import glob
import linecache
import random
import copy
from eulerianCycles import eulerianCycles
from kmerDebruijnGraph import kmerDebruijnGraph

def universalCircularString(k):
    k = int(k)
    print("universalCircularString started")
    #print("guk:",genUniversalKmers(k))
    graph = kmerDebruijnGraph(genUniversalKmers(k))
    #print("graph:", graph.split("\n"))
    r1 = eulerianCycles(graph.split("\n")).split("->")
    #print("epath",r1)
    res = ""
    for kmer in r1:
        #print("kmer:", kmer)
        if res =="":
            res = kmer
        else:
            res = res + kmer[-1:]
    #we are making a cycle, so the last bit of the string needs to be choped off
    #as it will be created when we loop back to the start
    #to do this we chop off k-1 chars from the end.
    return res[:-(k - 1)]

def genUniversalKmers(k):
    # return an list of all possible kmers
    if k > 1:
        zero = arrayCellAppend(genUniversalKmers(k - 1),"0")
        one = arrayCellAppend(genUniversalKmers(k - 1),"1")
        return zero + one
    else:
        return ["0","1"]

#append a char to every cell in an array
def arrayCellAppend(arr,letter):
    #print(arr)
    for cell in range(len(arr)):
        arr[cell] = arr[cell] + letter
    #print(arr)
    return arr



if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
            k = param[0]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(universalCircularString(k))
