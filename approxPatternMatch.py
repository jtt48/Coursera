import sys
import re
import json
import glob
import linecache

# cycle window of size (len pattern) through text.
# if window is <= errorNmb place start index in rString.
def approxPatternMatch(pattern, text, errorNmb):
    
    print("starting approxPatternMatch")
    count = 0
    rstring = ""
    window = len(pattern)

    for i in range(len(text)):
        if i == len(text) - (len(pattern) - 1):
            return rstring
        for j in range(len(pattern)):
            if pattern[j] != text[i+j]:
                count = count + 1
                #print(pattern[j], text[i+j])
        print(count, pattern, text[i:i+len(pattern)])
        if count <= int(errorNmb):
            print(count <= errorNmb)
            print("I: ",i, "Count: ", count, "Error Nmb: ", errorNmb)
            #rstring = rstring + str(i) + " "
            rstring = rstring + 1
        count = 0
    return rstring


with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        
        param = input.read().splitlines()
        
        pattern = param[0]
        text = param[1]
        d = param[2]
        
        output.write(approxPatternMatch(pattern,text,d))


