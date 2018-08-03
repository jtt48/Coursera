import sys
import re
import json
import glob
import linecache

def hammingDistance(s1, s2):
    
    #print("starting hammingDistance")
    count = 0
    rstring = ""
    #print(s1)
    #print(s2)
    if len(s1) != len(s2):
        print("string lengths do not match")
        return
    for i in range(len(s1)):
        if i == len(s1):
            return str(count)
        if s1[i] != s2[i]:
            count = count + 1
    return str(count)


if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
        
            s1 = param[0]
            s2 = param[1]
        
            output.write(hammingDistance(s1,s2))


