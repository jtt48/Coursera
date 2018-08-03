import sys
import re
import json
import glob
import linecache

# cycle window od size (len pattern) through text.
# if window is <= errorNmb place start index in rString.
def approxPatternCount(pattern, text, errorNmb):
    
   # print("starting approxPatternMatch")
   # print("Pattern: ", pattern, " Matching to: ", text)
    count = 0
    rstring = 0
    window = len(pattern)

    for i in range(len(text)):
        if i == len(text) - ((len(pattern) - 1)):
            break
        for j in range(len(pattern)):
        #    if j == len(pattern) - 1:
         #       break
          #  print(pattern[j], text[i+j])
            if pattern[j] != text[i+j]:
                count = count + 1
        
        # print(count, pattern, text[i:i+len(pattern)])
        if count <= int(errorNmb):
            #print(count <= errorNmb)
            #print("I: ",i, "Count: ", count, "Error Nmb: ", errorNmb)
            rstring = rstring + 1
        count = 0
        # print(" approxPatternMatch: ",rstring)
    
    return rstring



if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
            param = input.read().splitlines()
            pattern = param[0]
            text = param[1]
            d = param[2]
            output.write(str(approxPatternCount(pattern,text,d)))


