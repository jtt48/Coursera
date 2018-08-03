import sys
import re
import json
import glob
import linecache
from approcPatternCount import approxPatternCount
from reverseCompliment import reverseCompliment
# cycle window od size (len pattern) through text.
# if window is <= errorNmb place start index in rString.
def frequentWordsMismatch(text, k, errorNmb):
    
    print("starting frequentWordsMismatch")
    # print("text: ", text)
    count = 0
    highCount = 0
    rstring = ""


    k = int(k)
    # print("K: ",k)
    dict = {}
    kmers = allKmers(k)
    for i in range(len(kmers)):
        dict[kmers[i]] = 0

#    for i in range(len(text) - int(k) + 1):
 #       print("i + k",i + int(k))
  #      dict.setdefault(text[i:(i + int(k))], 0)

    keys = list(dict.keys())
    for j in keys:
        # print(j)
        if dict[j] <= 0:
            res = int(approxPatternCount(j,text,errorNmb))
            rv = reverseCompliment(j)
            res2 = int(approxPatternCount(rv,text,errorNmb))
            #print(res)
            dict[j] = res + res2
            dict[rv] = res + res2

   # for x in keys:
        #print(x, " Count: ", dict[x], " HC: ", highCount)
    # print("---------------")
   
    
    #for y in keys:
        #rv = reverseCompliment(y)
        #dict.setdefault(rv, 0)
        #if dict[rv] > 0:
           #print(dict[y], dict[rv])
           #dict[y] = (dict[y] + dict[rv])
            #dict[rv] = 0
    
    
    for x in keys:

        #print(x, " Count: ", dict[x], " HC: ", highCount)
        #if x == "ATGT" or x == "ACAT" or x == "GATG" or x == "ATGC":
        #    print("\n###\n")
        if dict[x] == highCount:
            rstring = rstring + " " + x
        if dict[x] > highCount:
            highCount = dict[x]
            rstring = x

    return rstring


def allKmers(k):
    if k == 1:
        return ["G","C","A","T"]
    re = reBuild("G",allKmers(k - 1))
    re.extend(reBuild("C",allKmers(k-1)))
    re.extend(reBuild("A",allKmers(k-1)))
    re.extend(reBuild("T",allKmers(k-1)))
    return re
 
def reBuild(letter,array):
    for i in range(len(array)):
        array[i] = letter + array[i]
    return array



with open(sys.argv[1], "r+") as input:
    with open("output2.txt", "w+") as output:
        
        param = input.read().splitlines()
        
        text = param[0]
        k = param[1]
        d = param[2]
        
        output.write(frequentWordsMismatch(text,k,d))


