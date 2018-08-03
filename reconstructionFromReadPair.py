import sys
import re
import json
import glob
import linecache
import random
import copy
from reconstructionProblem import reconstructionProblem

def reconstructionFromReadPair(text,k,d):
    k = int(k)
    d = int(d)
    #print("text", text)
    prefix = []
    suffix = []
    for str in text:
        arr = str.split("|")
        prefix.append(arr[0])
        suffix.append(arr[1])
    while True:
        # read in both parts of the pair
        #if random.randint(0,1) > 0:
        #    prefix.append(prefix.pop(0))
        #if random.randint(0,1) > 0:
        #    suffix.append(suffix.pop(0))
        #print("prefix", prefix)
        #print("suffix", suffix)
    #print(reconstructionProblem(prefix))
        r1 = reconstructionProblem(prefix)
        r2 = reconstructionProblem(suffix)
        print(r1)
        print(r2)
        #print(r1[(len(r1)/2):])
        #print(r2[:(len(r2)/2)])
    #r2 should match r1 halfway through the string
        print("Test:",r1[(k + d):],r2[:-(k + d)], "K:", k , "D", d)
        if r1[(k + d):] == r2[:-(k+d)]:
            res = r1 + r2[(k+d):]
            print(res)
            return res
        print("failed to create a proper string from pairs.")
   
if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
            k = param[0]
            d = param[1]
            text = param[2:]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(reconstructionFromReadPair(text,k,d))
